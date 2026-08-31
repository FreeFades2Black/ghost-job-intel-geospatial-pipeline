"""
Unit tests for Ghost Job Ingestion, Medallion Architecture, and Greenville SC Tech Hub & Public Enterprise Scrapers.
"""

from src.scrapers.ats_scraper import ATSScraper
from src.scrapers.ghost_news_scraper import GhostJobNewsScraper
from src.medallion.pipeline_bronze_ingestion import BronzeIngestionEngine
from src.medallion.pipeline_silver_lifecycle import SilverLifecycleEngine
from src.medallion.pipeline_gold_ghost_metrics import GoldGhostMetricsEngine
from src.config import TOP_100_PUBLIC_COMPANIES

def test_ats_scraper_greenville_and_tech_giants():
    """Verify ATS scraper successfully parses Top 10 Greenville SC companies and national tech giants."""
    scraper = ATSScraper()
    test_tokens = [
        "michelin", "bmw_tech", "ge_vernova", "lockheed_martin", 
        "scansource", "fluor", "td_synnex", "hubbell", "duke_energy", "prisma_health_tech",
        "google", "microsoft", "meta", "nvidia"
    ]
    for token in test_tokens:
        meta = next((c for c in TOP_100_PUBLIC_COMPANIES if c["token"] == token), None)
        assert meta is not None, f"Company {token} missing from config"
        res = scraper.scrape_company(meta)
        assert res["company_token"] == token
        assert res["job_count"] > 0
        assert "raw_payload" in res

def test_ghost_news_scraper():
    """Verify live OSINT and SEC ghost job intelligence harvesting."""
    scraper = GhostJobNewsScraper()
    news = scraper.scrape_live_news()
    assert len(news) >= 3
    assert any("Clarify Capital" in n["title"] for n in news)

def test_medallion_pipeline_execution():
    """Verify full Bronze -> Silver -> Gold execution across Greenville SC and tech companies."""
    bronze = BronzeIngestionEngine()
    b_res = bronze.run_bronze_ingestion(max_companies=15)
    assert b_res["status"] == "success"
    assert b_res["total_raw_jobs"] > 0

    silver = SilverLifecycleEngine()
    s_res = silver.run_silver_processing()
    assert s_res["status"] == "success"
    assert s_res["total_active_requisitions"] > 0

    gold = GoldGhostMetricsEngine()
    g_res = gold.run_gold_aggregation()
    assert g_res["status"] == "success"
    assert g_res["companies_evaluated"] >= 10
