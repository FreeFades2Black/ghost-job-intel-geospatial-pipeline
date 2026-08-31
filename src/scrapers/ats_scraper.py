"""
Gunslinger Lore: Chapter I - The Ghost Requisition Harvester
Polls public ATS boards (Greenhouse, Lever) for the Top 100 enterprise tech companies.
"""

import logging
import requests
import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)

class ATSScraper:
    """Scrapes public job boards across Greenhouse and Lever."""

    HEADERS = {
        "User-Agent": "GhostPostingsResearch/1.0 (frontier.scout@desertrange.org)",
        "Accept": "application/json"
    }

    def fetch_greenhouse_board(self, token: str) -> Optional[Dict[str, Any]]:
        """Query Greenhouse board API: https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true"""
        url = f"https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true"
        try:
            resp = requests.get(url, headers=self.HEADERS, timeout=10)
            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 404:
                logger.warning(f"Greenhouse board not found for token: {token}")
                return None
            else:
                logger.warning(f"Greenhouse returned HTTP {resp.status_code} for {token}")
                return None
        except Exception as e:
            logger.error(f"Error scraping Greenhouse token {token}: {e}")
            return None

    def fetch_lever_board(self, token: str) -> Optional[List[Dict[str, Any]]]:
        """Query Lever board API: https://api.lever.co/v0/postings/{token}?mode=json"""
        url = f"https://api.lever.co/v0/postings/{token}?mode=json"
        try:
            resp = requests.get(url, headers=self.HEADERS, timeout=10)
            if resp.status_code == 200:
                return resp.json()
            return None
        except Exception as e:
            logger.error(f"Error scraping Lever token {token}: {e}")
            return None

    def scrape_company(self, company_meta: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch raw snapshot for a company and standardize payload."""
        token = company_meta["token"]
        ats = company_meta.get("ats", "greenhouse")
        scraped_at = datetime.now(timezone.utc).isoformat()

        raw_payload = None
        job_count = 0

        if ats == "greenhouse":
            raw_payload = self.fetch_greenhouse_board(token)
            if raw_payload and "jobs" in raw_payload:
                job_count = len(raw_payload["jobs"])
        elif ats == "lever":
            raw_payload = self.fetch_lever_board(token)
            if raw_payload and isinstance(raw_payload, list):
                job_count = len(raw_payload)

        return {
            "company_token": token,
            "company_name": company_meta["name"],
            "ticker": company_meta.get("ticker", "N/A"),
            "hq_city": company_meta.get("hq_city", "San Francisco"),
            "hq_state": company_meta.get("hq_state", "CA"),
            "lat": company_meta.get("lat", 37.7749),
            "lon": company_meta.get("lon", -122.4194),
            "ats_type": ats,
            "scraped_at": scraped_at,
            "job_count": job_count,
            "raw_payload": raw_payload or {}
        }
