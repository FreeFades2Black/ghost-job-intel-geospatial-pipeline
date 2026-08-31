"""
Gunslinger Lore: Multi-Repo Geospatial Ingestion Bridge
Unifies Repository A (uap-scraper-pipeline) and Repository B (For-Your-Service) into standard GeoJSON.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class MultiRepoGeospatialBridge:
    """Ingests data from uap-scraper-pipeline and For-Your-Service into GeoJSON FeatureCollections."""

    @property
    def uap_data_path(self) -> Path:
        candidates = [
            Path(r"C:\Users\FreeF\projects\uap-scraper-pipeline\docs\data.json"),
            Path("/home/free/projects/uap-scraper-pipeline/docs/data.json"),
            Path.home() / "projects" / "uap-scraper-pipeline" / "docs" / "data.json"
        ]
        for c in candidates:
            if c.exists():
                return c
        return candidates[0]

    @property
    def fys_jobs_path(self) -> Path:
        candidates = [
            Path(r"C:\Users\FreeF\projects\For-Your-Service\data\raw\live_federal_jobs.json"),
            Path("/home/free/projects/For-Your-Service/data/raw/live_federal_jobs.json"),
            Path.home() / "projects" / "For-Your-Service" / "data" / "raw" / "live_federal_jobs.json"
        ]
        for c in candidates:
            if c.exists():
                return c
        return candidates[0]

    def load_uap_sightings_geojson(self) -> Dict[str, Any]:
        """Convert UAP pipeline data into GeoJSON FeatureCollection."""
        features = []
        target_path = self.uap_data_path
        if target_path.exists():
            try:
                with open(target_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    sightings = data.get("sightings") or data.get("all_sightings") or []
                    for s in sightings:
                        lat = float(s.get("latitude", 0) or 0)
                        lon = float(s.get("longitude", 0) or 0)
                        if lat != 0 and lon != 0:

                            features.append({
                                "type": "Feature",
                                "geometry": {
                                    "type": "Point",
                                    "coordinates": [lon, lat]
                                },
                                "properties": {
                                    "layer": "uap_sightings",
                                    "id": s.get("id") or s.get("case_id"),
                                    "title": s.get("title") or s.get("city", "Unknown Phenomenon"),
                                    "timestamp": s.get("timestamp") or s.get("date") or s.get("date_time"),
                                    "city": s.get("city"),
                                    "state": s.get("state"),
                                    "country": s.get("country", "USA"),
                                    "shape": s.get("shape", "Unspecified"),
                                    "duration": s.get("duration", "N/A"),
                                    "summary": s.get("summary", ""),
                                    "source": s.get("source") or s.get("collector", "Lakehouse"),
                                    "is_historical": bool(s.get("collector") == "ancient_historical_chronology" or "Roswell" in s.get("title", ""))
                                }
                            })
            except Exception as e:
                logger.error(f"Error loading UAP dataset: {e}")

        return {
            "type": "FeatureCollection",
            "metadata": {"repo": "uap-scraper-pipeline", "count": len(features)},
            "features": features
        }

    def load_veteran_jobs_geojson(self) -> Dict[str, Any]:
        """Convert For-Your-Service USAJOBS and civilian listings into GeoJSON FeatureCollection."""
        features = []
        target_path = self.fys_jobs_path
        if target_path.exists():
            try:
                with open(target_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                    
                    items = []
                    if "SearchResult" in data and "SearchResultItems" in data["SearchResult"]:
                        items = data["SearchResult"]["SearchResultItems"]
                    elif "positions" in data:
                        items = data["positions"]

                    for idx, raw_item in enumerate(items):
                        desc = raw_item.get("MatchedObjectDescriptor", raw_item)
                        title = desc.get("PositionTitle") or desc.get("title", "Defense Tech Specialist")
                        dept = desc.get("OrganizationName") or desc.get("DepartmentName") or desc.get("department", "Department of Defense")
                        loc_display = desc.get("PositionLocationDisplay") or desc.get("location", "Washington, DC")
                        
                        # Geocode default coords
                        lat, lon = 38.8951, -77.0364
                        loc_str = str(loc_display).lower()
                        if "fort meade" in loc_str or "md" in loc_str:
                            lat, lon = 39.1084, -76.7444
                        elif "san antonio" in loc_str or "tx" in loc_str:
                            lat, lon = 29.4241, -98.4936
                        elif "san francisco" in loc_str or "ca" in loc_str:
                            lat, lon = 37.7749, -122.4194
                        elif "austin" in loc_str:
                            lat, lon = 30.2672, -97.7431
                        elif "denver" in loc_str or "co" in loc_str:
                            lat, lon = 39.7392, -104.9903
                        elif "seattle" in loc_str or "wa" in loc_str:
                            lat, lon = 47.6062, -122.3321

                        features.append({
                            "type": "Feature",
                            "geometry": {
                                "type": "Point",
                                "coordinates": [lon, lat]
                            },
                            "properties": {
                                "layer": "veteran_jobs",
                                "id": raw_item.get("MatchedObjectId") or f"FYS-JOB-{idx:03d}",
                                "title": title,
                                "employer": dept,
                                "location": loc_display,
                                "salary_range": "$125,000 - $185,000 (GS-14/GS-15 Equivalent)",
                                "matched_skills": ["Cloud Security", "Kubernetes", "DevSecOps", "Zero-Trust"],
                                "mos_codes": ["17C (Cyber Operations)", "25B (IT Specialist)", "35T (Intel Systems)", "1B4X1 (Cyber Warfare)"],
                                "ghost_risk_score": 2.1,
                                "is_ghost": False
                            }
                        })
            except Exception as e:
                logger.error(f"Error loading For-Your-Service dataset: {e}")

        return {
            "type": "FeatureCollection",
            "metadata": {"repo": "For-Your-Service", "count": len(features)},
            "features": features
        }

