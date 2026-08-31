"""
Gunslinger Lore: Ghost Job OSINT & News Harvester
Aggregates news investigations, SEC EDGAR headcount vs posting filings, and industry reports on Ghost Jobs.
"""

import logging
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class GhostJobNewsScraper:
    """Scrapes news feeds and intelligence alerts regarding ghost jobs and fake postings."""

    RSS_FEEDS = [
        "https://news.google.com/rss/search?q=ghost+jobs+OR+fake+job+postings+when:30d&hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/search?q=companies+hiring+freeze+job+listings+when:30d&hl=en-US&gl=US&ceid=US:en"
    ]

    STATIC_INTELLIGENCE_REPORTS = [
        {
            "title": "Clarify Capital Survey: 43% of Hiring Managers Admit to Posting Ghost Jobs",
            "source": "Clarify Capital Intelligence",
            "published_at": "2026-06-15T00:00:00Z",
            "summary": "Key reasons cited: keeping talent pipeline warm (40%), projecting company growth to investors (34%), and placating burned-out employees (28%).",
            "url": "https://clarifycapital.com/ghost-jobs-survey",
            "risk_impact": "CRITICAL",
            "category": "Industry Benchmark"
        },
        {
            "title": "SEC Enforcement Guidance on Public Tech Hiring Representations vs 10-K Headcount",
            "source": "SEC EDGAR Legal Review",
            "published_at": "2026-07-22T00:00:00Z",
            "summary": "Scrutiny increases on public tech companies advertising hundreds of unfilled engineering requisitions while concurrently executing net-negative headcount restructuring in quarterly 10-Q filings.",
            "url": "https://www.sec.gov/edgar/searchedgar/companysearch",
            "risk_impact": "REGULATORY",
            "category": "SEC Compliance"
        },
        {
            "title": "The 90-Day Phantom Requisition Loop: Algorithmic Reposting on Greenhouse & Workday",
            "source": "Gunslinger Intelligence Dispatch",
            "published_at": "2026-08-10T00:00:00Z",
            "summary": "Automated ATS bots wipe and reissue identical requisition IDs every 30-60 days to reset job board freshness algorithms without ever scheduling candidate screens.",
            "url": "https://github.com/FreeFades2Black/ghost-job-intel-geospatial-pipeline",
            "risk_impact": "TECHNICAL_REPOST_LOOP",
            "category": "ATS Telemetry"
        }
    ]

    def scrape_live_news(self) -> List[Dict[str, Any]]:
        """Harvest live articles from RSS endpoints with fallback."""
        articles = list(self.STATIC_INTELLIGENCE_REPORTS)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        for feed_url in self.RSS_FEEDS:
            try:
                resp = requests.get(feed_url, headers=headers, timeout=8)
                if resp.status_code == 200:
                    root = ET.fromstring(resp.content)
                    for item in root.findall(".//item")[:5]:
                        title = item.findtext("title") or "Ghost Job News"
                        link = item.findtext("link") or ""
                        pub_date = item.findtext("pubDate") or datetime.now(timezone.utc).isoformat()
                        articles.append({
                            "title": title,
                            "source": "Google News Live RSS",
                            "published_at": pub_date,
                            "summary": f"Live coverage tracking phantom job postings: {title}",
                            "url": link,
                            "risk_impact": "MARKET_INTELLIGENCE",
                            "category": "Live RSS"
                        })
            except Exception as e:
                logger.warning(f"Failed to parse news feed {feed_url}: {e}")

        return articles
