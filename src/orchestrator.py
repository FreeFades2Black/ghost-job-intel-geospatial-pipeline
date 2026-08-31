"""
Gunslinger Lore: Master Medallion Pipeline & Multi-Repo Harvester
Runs the 3 Medallion Cylinders (Bronze -> Silver -> Gold) and builds GeoJSON layers.
"""

import logging
from src.medallion.pipeline_bronze_ingestion import BronzeIngestionEngine
from src.medallion.pipeline_silver_lifecycle import SilverLifecycleEngine
from src.medallion.pipeline_gold_ghost_metrics import GoldGhostMetricsEngine
from src.scrapers.ghost_news_scraper import GhostJobNewsScraper
from src.scrapers.multi_repo_bridge import MultiRepoGeospatialBridge

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("orchestrator")

class MasterFlywheelOrchestrator:
    """Executes the complete Medallion Flywheel and Multi-Repo Bridge."""

    def __init__(self):
        self.bronze_engine = BronzeIngestionEngine()
        self.silver_engine = SilverLifecycleEngine()
        self.gold_engine = GoldGhostMetricsEngine()
        self.news_scraper = GhostJobNewsScraper()
        self.bridge = MultiRepoGeospatialBridge()

    def run_full_flywheel(self, max_companies: int = 15):
        """Execute Bronze -> Silver -> Gold -> News -> GeoJSON Bridge."""
        logger.info("=" * 60)
        logger.info("🚀 Initiating Ghost Job Medallion Pipeline (Bronze -> Silver -> Gold)")
        logger.info("=" * 60)

        # Stage 1: Bronze
        b_res = self.bronze_engine.run_bronze_ingestion(max_companies=max_companies)
        logger.info(f"✅ Bronze Ingestion Complete: {b_res['total_raw_jobs']} raw jobs from {b_res['companies_polled']} companies.")

        # Stage 2: Silver
        s_res = self.silver_engine.run_silver_processing()
        logger.info(f"✅ Silver Normalization & SCD Type 2 Complete: {s_res['total_active_requisitions']} active requisitions.")

        # Stage 3: Gold
        g_res = self.gold_engine.run_gold_aggregation()
        logger.info(f"✅ Gold Aggregation Complete: Ghost Risk Index computed for {g_res['companies_analyzed']} companies.")

        # Stage 4: News & OSINT
        news = self.news_scraper.scrape_live_news()
        logger.info(f"✅ Ghost Job News Harvested: {len(news)} intelligence reports.")

        # Stage 5: GeoJSON Bridge
        uap_geojson = self.bridge.load_uap_sightings_geojson()
        jobs_geojson = self.bridge.load_veteran_jobs_geojson()
        logger.info(f"✅ Multi-Repo Bridge: {len(uap_geojson['features'])} UAP features, {len(jobs_geojson['features'])} Veteran Job features.")

        return {
            "bronze": b_res,
            "silver": s_res,
            "gold": g_res,
            "news_count": len(news),
            "uap_features": len(uap_geojson["features"]),
            "job_features": len(jobs_geojson["features"])
        }

if __name__ == "__main__":
    orchestrator = MasterFlywheelOrchestrator()
    orchestrator.run_full_flywheel()
