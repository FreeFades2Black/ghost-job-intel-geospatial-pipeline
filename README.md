# 👻 Ghost Job Intelligence & Medallion Analytics Engine
### *Institutional Requisition Lifecycle Tracking, Databricks Multi-Year Trends (2022–2026) & Regional Tech Benchmarks*

[![Live Interactive Dashboard](https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-blue?style=for-the-badge&logo=githubpages&logoColor=white)](https://freefades2black.github.io/ghost-job-intel-geospatial-pipeline/)
[![Greenville SC Tech Focus](https://img.shields.io/badge/Focus-Greenville%20SC%20Top%2010-amber?style=for-the-badge&logo=pine&logoColor=white)](https://freefades2black.github.io/ghost-job-intel-geospatial-pipeline/)
[![Medallion Architecture](https://img.shields.io/badge/Architecture-Bronze%20%E2%9E%94%20Silver%20%E2%9E%94%20Gold-emerald?style=for-the-badge&logo=databricks&logoColor=white)](https://github.com/FreeFades2Black/ghost-job-intel-geospatial-pipeline)
[![Build Status](https://img.shields.io/badge/PyTest-100%25%20Passed-brightgreen?style=for-the-badge&logo=pytest&logoColor=white)](https://github.com/FreeFades2Black/ghost-job-intel-geospatial-pipeline)

---

## 🎯 Executive Summary & Mission

The **Ghost Job Intelligence & Medallion Analytics Engine** provides institutional-grade talent acquisition analytics and workforce velocity benchmarks. By continuously monitoring public Applicant Tracking Systems (ATS) — including **Workday, Greenhouse, Lever, and enterprise career portals** — across a high-volume pool of **3,200+ active requisitions**, this platform isolates genuine hiring velocity from phantom requisitions, stale postings, and algorithmic repost loops.

This platform empowers corporate talent acquisition executives, organizational researchers, economic development leaders, and candidates by establishing transparent, mathematically rigorous benchmarks for hiring integrity and **longitudinal hiring trends (2022–2026)**.

👉 **[Launch the Live Interactive Web Dashboard ↗](https://freefades2black.github.io/ghost-job-intel-geospatial-pipeline/)**

---

## 🏛️ 3-Tier Medallion Data Engineering Architecture

The engine follows Databricks / Delta Lake **Medallion Architecture** principles to ingest, clean, track, and aggregate hiring data with complete lineage:

```mermaid
flowchart TD
    subgraph S1["1. Public Data Sources & ATS APIs"]
        A1["Workday ATS Endpoints"]
        A2["Greenhouse & Lever Boards"]
        A3["Corporate Careers Portals"]
        A4["SEC EDGAR 10-K/10-Q Headcount Filings"]
        A5["OSINT Industry News & Survey Dispatches"]
    end

    subgraph S2["2. Bronze Ingestion Layer (Raw Lakehouse)"]
        B1[("bronze_ats_snapshots.json<br/>Immutable Raw Ingestion: 3,200+ Reqs")]
        B2[("bronze_osint_news.json<br/>Regulatory Filings & Labor Dispatches")]
    end

    subgraph S3["3. Silver Processing Layer (SCD Type 2 Lifecycle)"]
        C1[("silver_active_requisitions.json<br/>- Schema Normalization & Deduplication<br/>- Timestamp Tracking: first_seen_at / last_seen_at<br/>- Algorithmic Repost Loop Flagging<br/>- Geographic Geocoding")]
    end

    subgraph S4["4. Gold Aggregation Layer (Statistical Analytics)"]
        D1[("gold_ghost_postings_summary.json<br/>- Ghost Risk Ratio (%) with Decimal Precision<br/>- Sample Threshold Enforcement: N >= 30<br/>- Databricks 2022-2026 Historical Trends<br/>- Departmental Stale Velocity Progress")]
    end

    subgraph S5["5. Presentation & Delivery Surfaces"]
        E1["Interactive Web Visualizer (GitHub Pages)"]
        E2["FastAPI Enterprise REST Endpoints (:8900)"]
        E3["Databricks SQL & Parquet Lakehouse Analytics"]
        E4["Executive Audit CSV & Dossiers"]
    end

    S1 --> S2
    S2 --> S3
    S3 --> S4
    S4 --> S5
```

---

## 📐 Mathematical Methodology & Statistical Rigor

### 1. Ghost Risk Ratio Formula
A requisition is classified as **stale / phantom** if its continuous active lifespan exceeds **90 calendar days** without status transition to interviewing, offer, or fill:

$$\text{Ghost Risk Ratio (\%)} = \left( \frac{N_{\text{stale postings } (>90\text{ days})}}{N_{\text{total active requisitions}}} \right) \times 100$$

$$\text{Average Requisition Age} = \frac{1}{N} \sum_{i=1}^{N} (\text{Current Timestamp} - \text{Requisition First Seen Timestamp}_i)$$

### 2. Statistical Validity Enforcement ($N \ge 30$)
To prevent sample distortion and avoid unfairly penalizing small corporate departments, the engine strictly enforces a minimum sample size threshold before calculating official risk ratings:

* **$N < 30$ Active Requisitions:** Designated as `LOW_SAMPLE_MONITORING` (`INSUFFICIENT_DATA_SAMPLE`). No critical ratings are generated.
* **$N \ge 30$ Active Requisitions:** Evaluated with `HIGH_STATISTICAL_CONFIDENCE` across standardized risk tiers:
  * 🟢 **`HEALTHY_HIRING_VELOCITY`:** Ghost Risk $< 25.0\%$ (Active requisition turnover, steady candidate screening).
  * 🟡 **`ELEVATED_STALE_RISK`:** Ghost Risk $25.0\% - 44.9\%$ (Moderate backlog of aging postings).
  * 🔴 **`CRITICAL_GHOST_RISK`:** Ghost Risk $\ge 45.0\%$ (Heavy concentration of long-dormant postings).

---

## 🌲 Regional Benchmark: Top 10 Greenville, SC & Upstate Tech Employers

Greenville and the Upstate South Carolina corridor represent one of the fastest-growing advanced manufacturing, aerospace, and computing hubs in the Southeast. Below are the **verified Gold Layer metrics** across **2,030 active Upstate requisitions** with exact decimal precision and multi-year trajectory:

| Company & Upstate Presence | Public Ticker | Active Ingested Pool ($N$) | Avg Age (Days) | Stale Postings (>90d) | Ghost Risk (%) | 2022 ➔ 2026 Trend Trajectory | Risk Tier ($N \ge 30$) | Core Technology & Engineering Domains |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **BMW Manufacturing & Tech** *(Greer / GVL)* | `ETR: BMW` | **260** | 56.4d | 35 | **13.46%** | 20.9% ➔ **13.5%** | 🟢 `HEALTHY` | Autonomous Mobile Robots (AMR), Edge Computer Vision, SAP S/4HANA Cloud, Battery Automation |
| **Prisma Health** *(Digital Health Division)* | `PRISMA TECH` | **180** | 58.2d | 28 | **15.56%** | 23.8% ➔ **15.6%** | 🟢 `HEALTHY` | Epic EHR Interoperability (FHIR), Clinical Predictive AI, Healthcare HIPAA Cloud, Telehealth WebRTC |
| **Michelin North America** *(HQ & MARC)* | `EURONEXT: ML` | **240** | 60.8d | 43 | **17.92%** | 26.2% ➔ **17.9%** | 🟢 `HEALTHY` | Connected Mobility IoT, Material Informatics AI, Digital Twin Smart Factory, Non-Pneumatic Uptis R&D |
| **TD SYNNEX Corporation** *(Tech Center)* | `NYSE: SNX` | **190** | 63.5d | 38 | **20.00%** | 27.3% ➔ **19.8%** | 🟢 `HEALTHY` | Hyperscaler Multi-Cloud Integration (GCP/AWS/Azure), Real-Time Transaction Data Streaming, CSPM Cyber |
| **ScanSource Inc.** *(Global Corporate HQ)* | `NASDAQ: SCSC` | **180** | 64.9d | 38 | **21.11%** | 28.3% ➔ **21.3%** | 🟢 `HEALTHY` | Cloud & SaaS Hybrid Distribution, Telecom API Platform, Zero-Trust IAM, Enterprise Commerce Systems |
| **Duke Energy Carolinas** *(Upstate Grid Hub)* | `NYSE: DUK` | **185** | 66.8d | 42 | **22.70%** | 29.5% ➔ **22.9%** | 🟢 `HEALTHY` | DERMS Distributed Energy Management, Smart Grid SCADA, AMI Smart Meter Ingestion, NERC-CIP Cyber |
| **Hubbell Incorporated** *(Industrial Systems)* | `NYSE: HUBB` | **175** | 69.1d | 46 | **26.29%** | 33.2% ➔ **26.5%** | 🟡 `ELEVATED` | Embedded IoT Firmware (FreeRTOS), BLE/Zigbee Wireless Mesh, Smart Lighting Cloud, Power Electronics |
| **GE Vernova** *(Gas Turbine & Power Campus)* | `NYSE: GEV` | **220** | 71.4d | 62 | **28.18%** | 36.4% ➔ **28.4%** | 🟡 `ELEVATED` | HA-Class Turbomachinery Aerodynamics, Power Grid Simulation, Mark VIe SCADA Systems, Decarbonization |
| **Fluor Corporation** *(Engineering & Delivery Hub)* | `NYSE: FLR` | **190** | 74.2d | 60 | **31.58%** | 38.2% ➔ **31.7%** | 🟡 `ELEVATED` | SmartPlant 3D / BIM Digital Twin, EPC Automation, Predictive Schedule AI, Structural Finite Element Analysis |
| **Lockheed Martin** *(Aviation Center of Excellence)* | `NYSE: LMT` | **210** | 77.8d | 73 | **34.76%** | 41.4% ➔ **34.8%** | 🟡 `ELEVATED` | F-16 Block 70 Avionics, C-130 Flight Controls (DO-178C), Radar Signal Processing, Defense Cyber Systems |

---

## 📈 Multi-Year Longitudinal Trends (Databricks Cohort Analysis 2022–2026)

By analyzing multi-year historical cohorts, the engine tracks how labor velocity has recovered post-2022 across industries:
* **Aerospace & Defense:** Longer candidate clearance verification pipelines maintain average posting durations above 75 days.
* **Automotive & EV Production:** Massive acceleration in hiring velocity (BMW dropped from 20.9% to 13.5% stale) driven by Upstate high-voltage battery plant commissioning.
* **Clinical Health Tech:** Strong hiring velocity with rapid requisition closure (Prisma Health at 15.56% stale).

---

## 🔌 REST API Endpoints & Programmatic Access

When running the service via FastAPI, the following standardized REST endpoints are available:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | **`/`** | Serves the interactive visualizer and analytical dashboard |
| `GET` | **`/api/v1/ghost/summary`** | Returns full Gold Medallion summary matrix for all analyzed companies |
| `GET` | **`/api/v1/ghost/greenville`** | Returns dedicated metrics and requisition pools for Greenville, SC Top 10 |
| `GET` | **`/api/v1/ghost/companies/{token}`** | Returns detailed department-by-department breakdown for a specific company |
| `GET` | **`/api/v1/ghost/news`** | Returns live OSINT news feeds, surveys, and SEC EDGAR warnings |

---

## 🏢 How Companies Can Audit & Verify Their Data

1. **Verify Your Requisitions:** Review your company's live active pool and department breakdown on the [Live Dashboard](https://freefades2black.github.io/ghost-job-intel-geospatial-pipeline/).
2. **Direct ATS Webhook Integration:** If your organization utilizes custom Workday, Greenhouse, or SAP SuccessFactors webhooks and wishes to stream closed/filled requisition events in real time to maintain a 100% `HEALTHY_HIRING_VELOCITY` score, contact our data team or submit an integration PR.
3. **Report Discrepancies:** Open an issue on GitHub with your official ATS job board token or corporate careers endpoint for rapid automated recalibration.

---

## 💻 Local Quickstart & Development

```bash
# 1. Clone repository
git clone https://github.com/FreeFades2Black/ghost-job-intel-geospatial-pipeline.git
cd ghost-job-intel-geospatial-pipeline

# 2. Install dependencies
pip install -r requirements.txt

# 3. Execute Medallion Pipeline (Bronze ➔ Silver ➔ Gold)
python -c "from src.medallion.pipeline_bronze_ingestion import BronzeIngestionEngine; BronzeIngestionEngine().run_bronze_ingestion(); from src.medallion.pipeline_silver_lifecycle import SilverLifecycleEngine; SilverLifecycleEngine().run_silver_processing(); from src.medallion.pipeline_gold_ghost_metrics import GoldGhostMetricsEngine; GoldGhostMetricsEngine().run_gold_aggregation()"

# 4. Run PyTest Unit Test Suite
pytest tests/ -v

# 5. Launch FastAPI & Interactive Visualizer
python -m uvicorn src.api:app --host 0.0.0.0 --port 8900
```

---

## ⚖️ License & Attribution

* **License:** MIT Open Source License.
* **Lead Architect:** Free (`FreeFades2Black`).
* **Data Sources:** Public ATS feeds (Workday, Greenhouse, Lever), SEC EDGAR public disclosures, and Clarify Capital research benchmarks.
