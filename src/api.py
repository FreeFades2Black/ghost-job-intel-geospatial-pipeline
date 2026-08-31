"""
Gunslinger Lore: FastAPI Ghost Job & Medallion Analytics API Server
Serves Gold Ghost Metrics, Top 100 Enterprise ATS Analytics, and OSINT News Feeds.
"""

from fastapi import FastAPI, Query, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
import json

from src.scrapers.ghost_news_scraper import GhostJobNewsScraper
from src.medallion.pipeline_gold_ghost_metrics import GoldGhostMetricsEngine
from src.medallion.pipeline_bronze_ingestion import BronzeIngestionEngine
from src.medallion.pipeline_silver_lifecycle import SilverLifecycleEngine
from src.config import GOLD_DIR, UI_DIR

app = FastAPI(
    title="Ghost Job Intelligence & Medallion Analytics API",
    description="Top 100 Public Companies ATS Harvester & Ghost Requisition Engine (Bronze -> Silver -> Gold)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

news_scraper = GhostJobNewsScraper()
gold_engine = GoldGhostMetricsEngine()
bronze_engine = BronzeIngestionEngine()
silver_engine = SilverLifecycleEngine()

@app.get("/", tags=["UI"])
def serve_ui():
    """Serve the interactive Ghost Job Intelligence dashboard."""
    index_path = UI_DIR / "index.html"
    return FileResponse(index_path)

@app.get("/api/v1/ghost/summary", tags=["Ghost Analytics"])
def get_ghost_analytics_summary():
    """Get Gold Medallion summary matrix for all analyzed companies."""
    gold_file = GOLD_DIR / "gold_ghost_postings_summary.json"
    if gold_file.exists():
        with open(gold_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.get("/api/v1/ghost/companies/{company_token}", tags=["Ghost Analytics"])
def get_company_ghost_profile(company_token: str):
    """Retrieve detailed ghost posting breakdown for a specific company."""
    summary = get_ghost_analytics_summary()
    for c in summary:
        if c.get("company_token") == company_token.lower():
            return {"status": "success", "company": c}
    return JSONResponse(status_code=404, content={"status": "not_found", "message": f"Company {company_token} not analyzed"})


@app.get("/api/v1/ghost/news", tags=["Ghost Analytics"])
def get_ghost_news_feed():
    """Scrape and return latest ghost job news, surveys, and SEC EDGAR warnings."""
    return news_scraper.scrape_live_news()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8900)
