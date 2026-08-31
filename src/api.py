"""
Gunslinger Lore: FastAPI Geospatial Server & Ghost Job Intelligence Bridge
Serves GeoJSON feeds, Gold Ghost Metrics, News Feeds, and Multi-Repo Visualizer.
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
import json

from src.scrapers.multi_repo_bridge import MultiRepoGeospatialBridge
from src.scrapers.ghost_news_scraper import GhostJobNewsScraper
from src.medallion.pipeline_gold_ghost_metrics import GoldGhostMetricsEngine
from src.config import GOLD_DIR, UI_DIR

app = FastAPI(
    title="Geospatial Multi-Repo & Ghost Job Intelligence API",
    description="Multi-layer visualizer bridging uap-scraper-pipeline, For-Your-Service, and Top 100 Public ATS Ghost Job Detection",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bridge = MultiRepoGeospatialBridge()
news_scraper = GhostJobNewsScraper()

@app.get("/", tags=["UI"])
def serve_ui():
    """Serve the interactive MapLibre / Leaflet multi-layer visualizer."""
    index_path = UI_DIR / "index.html"
    return FileResponse(index_path)

@app.get("/api/v1/geojson/uap", tags=["GeoJSON Bridge"])
def get_uap_geojson():
    """GeoJSON FeatureCollection of UAP sightings from Repository A."""
    return bridge.load_uap_sightings_geojson()

@app.get("/api/v1/geojson/veteran-jobs", tags=["GeoJSON Bridge"])
def get_veteran_jobs_geojson():
    """GeoJSON FeatureCollection of Veteran Transition jobs from Repository B."""
    return bridge.load_veteran_jobs_geojson()

@app.get("/api/v1/geojson/ghost-companies", tags=["GeoJSON Bridge"])
def get_ghost_companies_geojson():
    """GeoJSON FeatureCollection of Top 100 Companies tagged with Ghost Risk Index."""
    gold_file = GOLD_DIR / "gold_ghost_postings_summary.json"
    features = []
    if gold_file.exists():
        with open(gold_file, "r", encoding="utf-8") as f:
            summary = json.load(f)
            for c in summary:
                features.append({
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [c["lon"], c["lat"]]
                    },
                    "properties": {
                        "layer": "ghost_companies",
                        "company_name": c["company_name"],
                        "company_token": c["company_token"],
                        "total_listings": c["total_active_listings"],
                        "avg_age_days": c["avg_listing_age_days"],
                        "stale_over_90d": c["stale_listings_over_90d"],
                        "ghost_risk_pct": c["ghost_risk_pct"],
                        "risk_tier": c["risk_tier"],
                        "top_stale_role": c["top_stale_role"]
                    }
                })
    return {
        "type": "FeatureCollection",
        "metadata": {"layer": "ghost_companies", "count": len(features)},
        "features": features
    }

@app.get("/api/v1/ghost/summary", tags=["Ghost Analytics"])
def get_ghost_analytics_summary():
    """Get Gold Medallion summary matrix for all analyzed companies."""
    gold_file = GOLD_DIR / "gold_ghost_postings_summary.json"
    if gold_file.exists():
        with open(gold_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.get("/api/v1/ghost/news", tags=["Ghost Analytics"])
def get_ghost_news_feed():
    """Scrape and return latest ghost job news, surveys, and SEC EDGAR warnings."""
    return news_scraper.scrape_live_news()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8900)
