"""
Gunslinger Lore: Chapter I - The Sight Across the High Wastes (Bronze Ingestion)
Out on the frontier, the Gunslinger tracks the trails left by the rail-barons,
sifting true wagons from phantom dust storms.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any
from src.config import BRONZE_DIR, TOP_100_PUBLIC_COMPANIES
from src.scrapers.ats_scraper import ATSScraper

class BronzeIngestionEngine:
    """Ingests raw ATS snapshots into Bronze JSON / Parquet lakehouse tier."""

    def __init__(self):
        self.scraper = ATSScraper()

    def run_bronze_ingestion(self, max_companies: int = 15) -> Dict[str, Any]:
        """Fetch and stage Bronze snapshots for target public companies."""
        snapshots: List[Dict[str, Any]] = []
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

        for company in TOP_100_PUBLIC_COMPANIES[:max_companies]:
            result = self.scraper.scrape_company(company)
            snapshots.append(result)

        # Write Bronze Snapshot
        bronze_file = BRONZE_DIR / f"bronze_ats_snapshots_{timestamp}.json"
        with open(bronze_file, "w", encoding="utf-8") as f:
            json.dump(snapshots, f, indent=2)

        # Also write latest symlink
        latest_file = BRONZE_DIR / "bronze_ats_snapshots_latest.json"
        with open(latest_file, "w", encoding="utf-8") as f:
            json.dump(snapshots, f, indent=2)

        return {
            "status": "success",
            "tier": "BRONZE",
            "companies_polled": len(snapshots),
            "total_raw_jobs": sum(s["job_count"] for s in snapshots),
            "output_file": str(bronze_file)
        }
