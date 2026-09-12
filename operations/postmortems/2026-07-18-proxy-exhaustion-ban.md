# Incident Post-Mortem: ATS Scraper Proxy Pool Exhaustion Triggering 24-Hour Subnet Ban

**Incident Date:** 2026-07-18  
**Impact Duration:** 4 hours  
**Severity:** SEV-2  
**Root Cause:** A developer increased scraper concurrency from 8 to 64 workers without configuring session stickiness, causing 500 concurrent requests to hit Greenhouse ATS endpoints from a single residential provider subnet, triggering a 24-hour Cloudflare IP block.

## Timeline
* **04:00 UTC:** Scheduled morning scraper run initiated with 64 concurrent threads.
* **04:03 UTC:** Cloudflare returned HTTP 403 on 100% of outbound requests.
* **04:12 UTC:** Scraper failure rate alert paged on-call engineer.
* **04:25 UTC:** Crawl halted; traffic routed through secondary proxy provider with strict concurrency caps (max 8 per ATS domain).
* **08:00 UTC:** Full crawl completed at reduced concurrency.

## Corrective Actions
1. Implemented domain-level rate limiter restricting concurrency to max 8 requests/sec per target ATS host.
2. Configured proxy provider auto-rotation to failover to secondary provider when 403 error rate exceeds 2%.
