# 🌐 Ghost Job Intelligence & Multi-Repo Geospatial Visualizer

An automated, Medallion Architecture pipeline (Bronze ➔ Silver ➔ Gold) and open-source geospatial front-end bridging **Repository A (`uap-scraper-pipeline`)**, **Repository B (`For-Your-Service`)**, and public ATS boards (Greenhouse, Lever, Workday) for the **Top 100 Largest Public Tech Companies** to expose ghost postings, 90-day stale requisition loops, and OSINT news alerts.

---

## 🏛️ Medallion Architecture Overview

```mermaid
graph TD
    A[Public ATS Endpoints / Greenhouse / Lever] -->|Raw JSON Ingestion| B[(Bronze: bronze_ats_snapshots)]
    C[SEC EDGAR / News Feeds / OSINT] -->|Regulatory Filings| B
    D[Repo A: uap-scraper-pipeline] -->|Multi-Era Telemetry| M[Multi-Repo Bridge]
    E[Repo B: For-Your-Service] -->|Veteran MOS Requisitions| M
    B -->|Schema Flattening & SCD Type 2 Lifecycle| F[(Silver: silver_active_requisitions)]
    F -->|Ghost Index & Stale Metrics (>90d)| G[(Gold: gold_ghost_postings_summary)]
    M -->|Standard GeoJSON / OpenStreetMap| H[Interactive Geospatial Visualizer]
    G -->|Ghost Risk Hotspots| H
    H --> I[Omarchy Desktop & Databricks Dashboard]
```

---

## 🚀 Key Features

1. **Top 100 Public Companies Ghost Index:**
   - Real-time polling across public ATS APIs (GitLab, Block, Robinhood, Cloudflare, Datadog, Snowflake, CrowdStrike, Palantir, Coinbase, etc.).
   - SCD Type 2 lifecycle tracking recording `first_seen_at`, `last_seen_at`, and detecting algorithmic repost loops.
   - Calculates **Ghost Risk Ratio (%)** and flags listings active for $>90$ days.

2. **Ghost Job OSINT & News Scraper:**
   - Aggregates live RSS intelligence feeds, survey benchmarks (Clarify Capital), and SEC EDGAR headcount disclosure warnings.

3. **Multi-Repo Geospatial Bridge:**
   - Standard GeoJSON endpoints unifying:
     - 🛸 **UAP Sightings Layer:** 1,041+ sightings from 1480 BC to Present (Roswell 1947, Roman shields, Egyptian disks).
     - 🎖️ **Veteran Job Listings Layer:** Geo-tagged civilian job opportunities with MOS/AFSC crosswalk match.
     - 👻 **Corporate Ghost Hotspots:** Geospatial coordinate mapping of tech company HQs color-coded by Ghost Risk Index.

4. **Zero-Lock Open-Source Basemap:**
   - OpenStreetMap / CartoDB Dark tiles with Leaflet and marker clustering.

---

## 📊 Databricks SQL Dashboard Queries

```sql
-- Gold Layer Reckoning: Exposing Stale Ghost Requisitions (>90 Days)
SELECT 
    company_token,
    company_name,
    total_active_listings,
    ROUND(avg_listing_age_days, 1) AS avg_days_open,
    stale_listings_over_90d,
    ROUND(ghost_risk_pct, 2) AS ghost_risk_pct,
    risk_tier,
    top_stale_role
FROM gold_ghost_postings_summary
ORDER BY ghost_risk_pct DESC;
```

---

## 🛠️ Quickstart & Local Execution

```bash
# Clone & install dependencies
pip install -r requirements.txt

# Run full Medallion Flywheel (Bronze -> Silver -> Gold)
python -m src.orchestrator

# Launch FastAPI & Interactive Visualizer on port 8900
python -m src.api
```
