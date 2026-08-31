"""
Gunslinger Lore: Chapter III - The High Noon Ledger (Gold Ghost Metrics)
The final reckoning where phantom bounties exceeding ninety days are exposed,
revealing the true velocity of the frontier saloon with focus on Greenville, SC Top 10 Public & Tech Employers.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any
from src.config import SILVER_DIR, GOLD_DIR

class GoldGhostMetricsEngine:
    """Aggregates ghost job indices, stale posting durations, and posting-to-headcount anomalies."""

    def run_gold_aggregation(self) -> Dict[str, Any]:
        """Calculates Ghost Risk Index (>90 days active) across companies and departments."""
        silver_file = SILVER_DIR / "silver_active_requisitions.json"
        if not silver_file.exists():
            return {"status": "error", "message": "Silver layer missing"}

        with open(silver_file, "r", encoding="utf-8") as f:
            silver_records = json.load(f)

        now = datetime.now(timezone.utc)
        company_stats: Dict[str, Dict[str, Any]] = {}

        for r in silver_records:
            token = r["company_token"]
            name = r["company_name"]
            
            try:
                first_seen = datetime.fromisoformat(r["first_seen_at"].replace("Z", "+00:00"))
                days_active = max(1, (now - first_seen).days)
            except Exception:
                days_active = 30

            is_stale = 1 if days_active > 90 else 0

            if token not in company_stats:
                company_stats[token] = {
                    "company_token": token,
                    "company_name": name,
                    "ticker": r.get("ticker", "N/A"),
                    "region": r.get("region", "National / Global"),
                    "hq_city": r.get("hq_city", "San Francisco"),
                    "hq_state": r.get("hq_state", "CA"),
                    "lat": r.get("lat", 37.7749),
                    "lon": r.get("lon", -122.4194),
                    "description": r.get("description", ""),
                    "total_active_listings": 0,
                    "total_days_sum": 0,
                    "stale_listings_over_90d": 0,
                    "department_breakdown": {},
                    "roles": []
                }

            dept = r.get("department_name", "General Engineering")
            if dept not in company_stats[token]["department_breakdown"]:
                company_stats[token]["department_breakdown"][dept] = {"total": 0, "stale": 0}
            company_stats[token]["department_breakdown"][dept]["total"] += 1
            company_stats[token]["department_breakdown"][dept]["stale"] += is_stale

            company_stats[token]["total_active_listings"] += 1
            company_stats[token]["total_days_sum"] += days_active
            company_stats[token]["stale_listings_over_90d"] += is_stale
            company_stats[token]["roles"].append({
                "req_id": r.get("requisition_id", ""),
                "title": r["job_title"],
                "dept": dept,
                "location": r.get("location_name", "Remote"),
                "days_active": days_active,
                "is_stale": bool(is_stale)
            })

        gold_summary = []
        for token, stats in company_stats.items():
            total = stats["total_active_listings"]
            avg_days = round(stats["total_days_sum"] / total, 1) if total > 0 else 0
            stale = stats["stale_listings_over_90d"]
            ghost_pct = round((stale / total) * 100, 2) if total > 0 else 0.0

            # Statistical Minimum Sample Size Enforcement (Databricks Rigor)
            MIN_SAMPLE_THRESHOLD = 30
            
            if total < MIN_SAMPLE_THRESHOLD:
                risk_tier = "LOW_SAMPLE_MONITORING"
                confidence = "INSUFFICIENT_DATA_SAMPLE"
            elif ghost_pct >= 45.0:
                risk_tier = "CRITICAL_GHOST_RISK"
                confidence = "HIGH_STATISTICAL_CONFIDENCE"
            elif ghost_pct >= 25.0:
                risk_tier = "ELEVATED_STALE_RISK"
                confidence = "HIGH_STATISTICAL_CONFIDENCE"
            else:
                risk_tier = "HEALTHY_HIRING_VELOCITY"
                confidence = "HIGH_STATISTICAL_CONFIDENCE"

            gold_summary.append({
                "company_token": token,
                "company_name": stats["company_name"],
                "ticker": stats["ticker"],
                "region": stats["region"],
                "hq_city": stats["hq_city"],
                "hq_state": stats["hq_state"],
                "lat": stats["lat"],
                "lon": stats["lon"],
                "description": stats["description"],
                "total_active_listings": total,
                "avg_listing_age_days": avg_days,
                "stale_listings_over_90d": stale,
                "ghost_risk_pct": ghost_pct,
                "risk_tier": risk_tier,
                "sample_confidence": confidence,
                "top_stale_role": next((x["title"] for x in stats["roles"] if x["is_stale"]), "N/A"),
                "department_breakdown": stats["department_breakdown"],
                "sample_roles": stats["roles"][:15]
            })

        # Sort descending by ghost_risk_pct
        gold_summary.sort(key=lambda x: x["ghost_risk_pct"], reverse=True)

        gold_file = GOLD_DIR / "gold_ghost_postings_summary.json"
        with open(gold_file, "w", encoding="utf-8") as f:
            json.dump(gold_summary, f, indent=2)

        return {
            "status": "success",
            "tier": "GOLD",
            "companies_evaluated": len(gold_summary),
            "output_file": str(gold_file)
        }
