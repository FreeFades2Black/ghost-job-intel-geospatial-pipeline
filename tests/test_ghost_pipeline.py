"""
Unit tests for Ghost Job Ingestion, Medallion Architecture, and Tech / Industrial Scrapers.
"""

from src.scrapers.ats_scraper import ATSScraper
from src.scrapers.ghost_news_scraper import GhostJobNewsScraper
from src.medallion.pipeline_bronze_ingestion import BronzeIngestionEngine
from src.medallion.pipeline_silver_lifecycle import SilverLifecycleEngine
from src.medallion.pipeline_gold_ghost_metrics import GoldGhostMetricsEngine
from src.config import TOP_100_PUBLIC_COMPANIES

def test_ats_scraper_mega_caps_and_industrials():
    """Verify ATS scraper successfully parses Google, Microsoft, Meta, NVIDIA, Walmart, Goodyear, Michelin, and GE."""
    scraper = ATSScraper()
    test_tokens = ["google", "microsoft", "meta", "nvidia", "walmart", "goodyear", "michelin", "ge"]
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
    """Verify full Bronze -> Silver -> Gold execution across tech and industrial companies."""
    bronze = BronzeIngestionEngine()
    b_res = bronze.run_bronze_ingestion(max_companies=10)
    assert b_res["status"] == "success"
    assert b_res["total_raw_jobs"] > 0

    silver = SilverLifecycleEngine()
    s_res = silver.run_silver_processing()
    assert s_res["status"] == "success"
    assert s_res["total_active_requisitions"] > 0

    gold = GoldGhostMetricsEngine()
    g_res = gold.run_gold_aggregation()
    assert g_res["status"] == "success"
    assert len(g_res["summary"]) >= 5

