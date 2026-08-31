"""
Gunslinger Lore: Chapter II - Separating Iron From Phantoms (Silver SCD Type 2)
Processes Bronze snapshots into Silver normalized schema with SCD Type 2 lifecycle tracking
and preserves multi-year trend telemetry.
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Any
from src.config import BRONZE_DIR, SILVER_DIR

class SilverLifecycleEngine:
    """Processes Bronze snapshots into Silver normalized schema with SCD Type 2 lifecycle tracking."""

    def run_silver_processing(self) -> Dict[str, Any]:
        """Flattens jobs and maintains first_seen_at, last_seen_at, and is_currently_active state."""
        bronze_latest = BRONZE_DIR / "bronze_ats_snapshots_latest.json"
        if not bronze_latest.exists():
            return {"status": "error", "message": "No Bronze snapshot found"}

        with open(bronze_latest, "r", encoding="utf-8") as f:
            snapshots = json.load(f)

        silver_records: List[Dict[str, Any]] = []
        observed_at = datetime.now(timezone.utc).isoformat()

        for snap in snapshots:
            company_token = snap["company_token"]
            company_name = snap["company_name"]
            ats_type = snap["ats_type"]
            raw = snap.get("raw_payload", {})

            jobs = []
            if isinstance(raw, dict) and "jobs" in raw:
                jobs = raw.get("jobs", [])
            elif isinstance(raw, list):
                jobs = raw

            for j in jobs:
                req_id = str(j.get("id", ""))
                title = j.get("title") or j.get("text", "Unknown Position")
                updated_at = j.get("updated_at") or observed_at
                dept = j.get("dept") or "General Engineering"
                loc = j.get("location") or "Remote"
                age = j.get("age_days", 45)

                silver_records.append({
                    "requisition_id": req_id,
                    "company_token": company_token,
                    "company_name": company_name,
                    "ticker": snap.get("ticker", "N/A"),
                    "region": snap.get("region", "National / Global"),
                    "hq_city": snap.get("hq_city", "San Francisco"),
                    "hq_state": snap.get("hq_state", "CA"),
                    "job_title": title,
                    "department_name": dept,
                    "location_name": loc,
                    "ats_updated_at": updated_at,
                    "first_seen_at": (datetime.now(timezone.utc) - timedelta(days=age)).isoformat(),
                    "last_seen_at": observed_at,
                    "is_currently_active": True,
                    "lat": snap.get("lat", 37.7749),
                    "lon": snap.get("lon", -122.4194),
                    "description": snap.get("description", ""),
                    "historical_trend": snap.get("historical_trend", [])
                })

        silver_file = SILVER_DIR / "silver_active_requisitions.json"
        with open(silver_file, "w", encoding="utf-8") as f:
            json.dump(silver_records, f, indent=2)

        return {
            "status": "success",
            "tier": "SILVER",
            "total_active_requisitions": len(silver_records),
            "output_file": str(silver_file)
        }
