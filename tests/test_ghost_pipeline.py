"""
Unit tests for Ghost Job Ingestion, Medallion Architecture, and Multi-Repo Geospatial Bridge.
"""

from src.scrapers.ats_scraper import ATSScraper
from src.scrapers.ghost_news_scraper import GhostJobNewsScraper
from src.scrapers.multi_repo_bridge import MultiRepoGeospatialBridge
from src.medallion.pipeline_bronze_ingestion import BronzeIngestionEngine
from src.medallion.pipeline_silver_lifecycle import SilverLifecycleEngine
from src.medallion.pipeline_gold_ghost_metrics import GoldGhostMetricsEngine

def test_ats_scraper_structure():
    scraper = ATSScraper()
    meta = {"token": "gitlab", "name": "GitLab Inc.", "ats": "greenhouse"}
    res = scraper.scrape_company(meta)
    assert res["company_token"] == "gitlab"
    assert "job_count" in res

def test_ghost_news_scraper():
    scraper = GhostJobNewsScraper()
    news = scraper.scrape_live_news()
    assert len(news) >= 3
    assert any("Clarify Capital" in n["title"] for n in news)

def test_multi_repo_bridge():
    bridge = MultiRepoGeospatialBridge()
    uap_geojson = bridge.load_uap_sightings_geojson()
    jobs_geojson = bridge.load_veteran_jobs_geojson()
    assert uap_geojson["type"] == "FeatureCollection"
    assert jobs_geojson["type"] == "FeatureCollection"
    assert len(uap_geojson["features"]) > 0

def test_medallion_pipeline_execution():
    bronze = BronzeIngestionEngine()
    b_res = bronze.run_bronze_ingestion(max_companies=3)
    assert b_res["status"] == "success"

    silver = SilverLifecycleEngine()
    s_res = silver.run_silver_processing()
    assert s_res["status"] == "success"

    gold = GoldGhostMetricsEngine()
    g_res = gold.run_gold_aggregation()
    assert g_res["status"] == "success"
    assert len(g_res["summary"]) > 0
