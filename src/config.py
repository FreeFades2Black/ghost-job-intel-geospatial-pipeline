"""
Gunslinger Lore: Ghost Postings & Geospatial Intelligence - Central Configuration
Defines endpoints, storage layers, and token registry for Top 100 Public Enterprise Companies.
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
    # Top Global Mega-Caps & Industrial Giants
    {"token": "google", "name": "Google (Alphabet Inc.)", "ats": "corporate_api", "ticker": "GOOGL", "hq_city": "Mountain View", "hq_state": "CA", "lat": 37.4220, "lon": -122.0841},
    {"token": "microsoft", "name": "Microsoft Corporation", "ats": "corporate_api", "ticker": "MSFT", "hq_city": "Redmond", "hq_state": "WA", "lat": 47.6740, "lon": -122.1215},
    {"token": "meta", "name": "Meta Platforms Inc.", "ats": "corporate_api", "ticker": "META", "hq_city": "Menlo Park", "hq_state": "CA", "lat": 37.4538, "lon": -122.1822},
    {"token": "nvidia", "name": "NVIDIA Corporation", "ats": "workday", "ticker": "NVDA", "hq_city": "Santa Clara", "hq_state": "CA", "lat": 37.3541, "lon": -121.9552},
    {"token": "walmart", "name": "Walmart Inc. (Global Tech)", "ats": "workday", "ticker": "WMT", "hq_city": "Bentonville", "hq_state": "AR", "lat": 36.3729, "lon": -94.2088},
    {"token": "goodyear", "name": "The Goodyear Tire & Rubber Co.", "ats": "workday", "ticker": "GT", "hq_city": "Akron", "hq_state": "OH", "lat": 41.0814, "lon": -81.5190},
    {"token": "michelin", "name": "Michelin Group", "ats": "workday", "ticker": "ML.PA", "hq_city": "Greenville / Clermont", "hq_state": "SC", "lat": 34.8526, "lon": -82.3940},
    {"token": "ge", "name": "General Electric (GE Aerospace)", "ats": "workday", "ticker": "GE", "hq_city": "Evendale / Boston", "hq_state": "OH", "lat": 39.2456, "lon": -84.4530},
    
    # Public Cloud, SaaS & High-Growth Tech
    {"token": "gitlab", "name": "GitLab Inc.", "ats": "greenhouse", "ticker": "GTLB", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "block", "name": "Block Inc.", "ats": "greenhouse", "ticker": "SQ", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "robinhood", "name": "Robinhood Markets", "ats": "greenhouse", "ticker": "HOOD", "hq_city": "Menlo Park", "hq_state": "CA", "lat": 37.4538, "lon": -122.1822},
    {"token": "cloudflare", "name": "Cloudflare Inc.", "ats": "greenhouse", "ticker": "NET", "hq_city": "Austin", "hq_state": "TX", "lat": 30.2672, "lon": -97.7431},

    {"token": "datadog", "name": "Datadog Inc.", "ats": "greenhouse", "ticker": "DDOG", "hq_city": "New York", "hq_state": "NY", "lat": 40.7128, "lon": -74.0060},
    {"token": "snowflake", "name": "Snowflake Inc.", "ats": "greenhouse", "ticker": "SNOW", "hq_city": "Bozeman", "hq_state": "MT", "lat": 45.6770, "lon": -111.0429},
    {"token": "crowdstrike", "name": "CrowdStrike Holdings", "ats": "greenhouse", "ticker": "CRWD", "hq_city": "Austin", "hq_state": "TX", "lat": 30.2672, "lon": -97.7431},
    {"token": "palantir", "name": "Palantir Technologies", "ats": "greenhouse", "ticker": "PLTR", "hq_city": "Denver", "hq_state": "CO", "lat": 39.7392, "lon": -104.9903},
    {"token": "coinbase", "name": "Coinbase Global", "ats": "greenhouse", "ticker": "COIN", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "stripe", "name": "Stripe Inc.", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "South San Francisco", "hq_state": "CA", "lat": 37.6547, "lon": -122.4077},
    {"token": "doordash", "name": "DoorDash Inc.", "ats": "greenhouse", "ticker": "DASH", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "uber", "name": "Uber Technologies", "ats": "greenhouse", "ticker": "UBER", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "airbnb", "name": "Airbnb Inc.", "ats": "greenhouse", "ticker": "ABNB", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "lyft", "name": "Lyft Inc.", "ats": "greenhouse", "ticker": "LYFT", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "pinterest", "name": "Pinterest Inc.", "ats": "greenhouse", "ticker": "PINS", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "reddit", "name": "Reddit Inc.", "ats": "greenhouse", "ticker": "RDDT", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "mongodb", "name": "MongoDB Inc.", "ats": "greenhouse", "ticker": "MDB", "hq_city": "New York", "hq_state": "NY", "lat": 40.7128, "lon": -74.0060},
    {"token": "elastic", "name": "Elastic N.V.", "ats": "greenhouse", "ticker": "ESTC", "hq_city": "Mountain View", "hq_state": "CA", "lat": 37.3861, "lon": -122.0839},
    {"token": "okta", "name": "Okta Inc.", "ats": "greenhouse", "ticker": "OKTA", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "twilio", "name": "Twilio Inc.", "ats": "greenhouse", "ticker": "TWLO", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "zoom", "name": "Zoom Video Communications", "ats": "greenhouse", "ticker": "ZM", "hq_city": "San Jose", "hq_state": "CA", "lat": 37.3382, "lon": -121.8863},
    {"token": "box", "name": "Box Inc.", "ats": "greenhouse", "ticker": "BOX", "hq_city": "Redwood City", "hq_state": "CA", "lat": 37.4852, "lon": -122.2364},
    {"token": "dropbox", "name": "Dropbox Inc.", "ats": "greenhouse", "ticker": "DBX", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "hubspot", "name": "HubSpot Inc.", "ats": "greenhouse", "ticker": "HUBS", "hq_city": "Cambridge", "hq_state": "MA", "lat": 42.3736, "lon": -71.1097},
    {"token": "atlassian", "name": "Atlassian Corp", "ats": "lever", "ticker": "TEAM", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "figma", "name": "Figma Inc.", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "notion", "name": "Notion Labs", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "scaleai", "name": "Scale AI", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "openai", "name": "OpenAI", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "anthropic", "name": "Anthropic PBC", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "databricks", "name": "Databricks Inc.", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "gusto", "name": "Gusto", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "Denver", "hq_state": "CO", "lat": 39.7392, "lon": -104.9903},
    {"token": "plaid", "name": "Plaid Inc.", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "chime", "name": "Chime Financial", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "ripple", "name": "Ripple Labs", "ats": "greenhouse", "ticker": "PRIVATE", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "unity", "name": "Unity Software", "ats": "greenhouse", "ticker": "U", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "roblox", "name": "Roblox Corp", "ats": "greenhouse", "ticker": "RBLX", "hq_city": "San Mateo", "hq_state": "CA", "lat": 37.5630, "lon": -122.3255},
    {"token": "affirm", "name": "Affirm Holdings", "ats": "greenhouse", "ticker": "AFRM", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "sofi", "name": "SoFi Technologies", "ats": "greenhouse", "ticker": "SOFI", "hq_city": "San Francisco", "hq_state": "CA", "lat": 37.7749, "lon": -122.4194},
    {"token": "toast", "name": "Toast Inc.", "ats": "greenhouse", "ticker": "TOST", "hq_city": "Boston", "hq_state": "MA", "lat": 42.3601, "lon": -71.0589},
]
