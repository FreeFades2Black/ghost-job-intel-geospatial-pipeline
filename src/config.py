"""
Gunslinger Lore: Ghost Postings & Geospatial Intelligence - Central Configuration
Defines endpoints, storage layers, and token registry for Top Public Enterprise Companies & Greenville SC Tech Hubs.
"""

from pathlib import Path
from typing import Dict, List

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"
UI_DIR = BASE_DIR / "ui"

for d in [BRONZE_DIR, SILVER_DIR, GOLD_DIR, UI_DIR]:
    d.mkdir(parents=True, exist_ok=True)

TOP_100_PUBLIC_COMPANIES: List[Dict[str, str]] = [
    # =========================================================================
    # 🌲 GREENVILLE, SC & UPSTATE TECHNOLOGY CORRIDOR (TOP 10 PUBLIC & TECH HUBS)
    # =========================================================================
    {
        "token": "michelin",
        "name": "Michelin North America",
        "ats": "workday",
        "ticker": "ML.PA",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8526,
        "lon": -82.3940,
        "description": "North American Corporate HQ & Americas R&D Corp (MARC) - Connected Mobility, Material Informatics & Smart Factory."
    },
    {
        "token": "bmw_tech",
        "name": "BMW Manufacturing & Tech Center",
        "ats": "workday",
        "ticker": "BMWYY",
        "hq_city": "Greer / Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8957,
        "lon": -82.2189,
        "description": "Plant Spartanburg & IT Operations Center - Industrial AI, Autonomous Robotics (AMR), Edge Computer Vision & SAP Cloud."
    },
    {
        "token": "ge_vernova",
        "name": "GE Vernova (Power & Gas Turbines)",
        "ats": "workday",
        "ticker": "GEV",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8214,
        "lon": -82.3392,
        "description": "Global Gas Turbine R&D & Advanced Manufacturing Campus - Power Grid Simulation, Turbomachinery Aerodynamics & SCADA."
    },
    {
        "token": "lockheed_martin",
        "name": "Lockheed Martin (Aviation Center)",
        "ats": "workday",
        "ticker": "LMT",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.7479,
        "lon": -82.3787,
        "description": "Greenville Operations Center of Excellence - F-16 Block 70 Avionics, C-130 Flight Critical Software & Aerospace Cyber."
    },
    {
        "token": "scansource",
        "name": "ScanSource Inc.",
        "ats": "workday",
        "ticker": "SCSC",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8682,
        "lon": -82.3256,
        "description": "Global Corporate Headquarters - Fortune 1000 Cloud & SaaS Hybrid Distribution, Telecom API Platforms & Cyber Systems."
    },
    {
        "token": "fluor",
        "name": "Fluor Corporation",
        "ats": "workday",
        "ticker": "FLR",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8398,
        "lon": -82.3121,
        "description": "Greenville Mega-Project Delivery & Engineering Office - Advanced BIM Digital Twin, Project Analytics & Plant Automation."
    },
    {
        "token": "td_synnex",
        "name": "TD SYNNEX Corporation",
        "ats": "workday",
        "ticker": "SNX",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8526,
        "lon": -82.3940,
        "description": "Enterprise Technology Operations Campus - Hyperscaler Multi-Cloud Integration, Cybersecurity & SaaS Commerce Platforms."
    },
    {
        "token": "hubbell",
        "name": "Hubbell Incorporated",
        "ats": "workday",
        "ticker": "HUBB",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8197,
        "lon": -82.3340,
        "description": "Commercial & Industrial Lighting / Electrical Systems - Smart Lighting IoT Firmware, Wireless Mesh & Power Electronics."
    },
    {
        "token": "duke_energy",
        "name": "Duke Energy Carolinas",
        "ats": "workday",
        "ticker": "DUK",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8510,
        "lon": -82.3980,
        "description": "Upstate SC Grid Operations & Power Tech - Grid Modernization, Smart Meter IoT Ingestion, DERMS & Substation SCADA."
    },
    {
        "token": "prisma_health_tech",
        "name": "Prisma Health (Digital Health)",
        "ats": "workday",
        "ticker": "PRISMA",
        "hq_city": "Greenville",
        "hq_state": "SC",
        "region": "Greenville / Upstate SC",
        "lat": 34.8228,
        "lon": -82.4082,
        "description": "Upstate Biomedical Computing & Health Tech - Epic EHR FHIR Integration, Clinical Predictive AI & Telehealth Cloud."
    },

    # =========================================================================
    # 🚀 GLOBAL MEGA-CAPS & ENTERPRISE TECH GIANTS
    # =========================================================================
    {"token": "google", "name": "Google (Alphabet Inc.)", "ats": "corporate_api", "ticker": "GOOGL", "hq_city": "Mountain View", "hq_state": "CA", "region": "Silicon Valley / West Coast", "lat": 37.4220, "lon": -122.0841, "description": "Cloud Spanner, Gemini Multimodal Foundations, DeepMind TPU Fleet & Android Security."},
    {"token": "microsoft", "name": "Microsoft Corporation", "ats": "corporate_api", "ticker": "MSFT", "hq_city": "Redmond", "hq_state": "WA", "region": "Pacific Northwest", "lat": 47.6740, "lon": -122.1215, "description": "Azure Core Systems, Copilot Studio, Defender XDR, Entra ID & Datacenter Automation."},
    {"token": "meta", "name": "Meta Platforms Inc.", "ats": "corporate_api", "ticker": "META", "hq_city": "Menlo Park", "hq_state": "CA", "region": "Silicon Valley / West Coast", "lat": 37.4538, "lon": -122.1822, "description": "AI PyTorch Fleet, Reality Labs Quest Optics, WhatsApp Real-Time & Privacy Ad Tech."},
    {"token": "nvidia", "name": "NVIDIA Corporation", "ats": "workday", "ticker": "NVDA", "hq_city": "Santa Clara", "hq_state": "CA", "region": "Silicon Valley / West Coast", "lat": 37.3541, "lon": -121.9552, "description": "CUDA Compiler LLVM, Blackwell DL Performance, DRIVE Autonomous Vehicles & Isaac Robotics."},
    {"token": "walmart", "name": "Walmart Inc. (Global Tech)", "ats": "workday", "ticker": "WMT", "hq_city": "Bentonville", "hq_state": "AR", "region": "Midwest / South", "lat": 36.3729, "lon": -94.2088, "description": "Omni-Channel Delta Lake, Supply Chain Automation Robotics, Edge Kubernetes & Zero-Trust IAM."},
    {"token": "goodyear", "name": "The Goodyear Tire & Rubber Co.", "ats": "workday", "ticker": "GT", "hq_city": "Akron", "hq_state": "OH", "region": "Midwest / Industrial", "lat": 41.0814, "lon": -81.5190, "description": "Goodyear SightLine IoT, Smart Factory Robotics, FEA Simulation & Compound Modeling."},
    {"token": "cloudflare", "name": "Cloudflare Inc.", "ats": "greenhouse", "ticker": "NET", "hq_city": "Austin", "hq_state": "TX", "region": "Texas Tech Hub", "lat": 30.2672, "lon": -97.7431, "description": "Global Edge CDN, Zero-Trust Access, DDoS Defense & Serverless Workers."},
    {"token": "datadog", "name": "Datadog Inc.", "ats": "greenhouse", "ticker": "DDOG", "hq_city": "New York", "hq_state": "NY", "region": "East Coast Tech", "lat": 40.7128, "lon": -74.0060, "description": "Cloud Observability, APM Distributed Tracing, Security Monitoring & LLM Observability."},
    {"token": "snowflake", "name": "Snowflake Inc.", "ats": "greenhouse", "ticker": "SNOW", "hq_city": "Bozeman", "hq_state": "MT", "region": "Mountain West", "lat": 45.6770, "lon": -111.0429, "description": "Data Cloud Warehouse, Snowpark ML, Iceberg Lakehouse & Native App Framework."},
    {"token": "palantir", "name": "Palantir Technologies", "ats": "greenhouse", "ticker": "PLTR", "hq_city": "Denver", "hq_state": "CO", "region": "Mountain West / Defense", "lat": 39.7392, "lon": -104.9903, "description": "Foundry Enterprise Ontology, AIP Generative Defense & Gotham Mission Systems."}
]
