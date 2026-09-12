# Operational Runbook: Diagnosing Cloudflare Captcha Spikes & Proxy Pool Exhaustion

**Severity:** P2 / Scraper Pipeline Throttled  
**Target Systems:** Headless Crawler Pool, Residential Proxy Gateway, ATS Scraper

## Diagnostic Workflow

### 1. Check HTTP Status Distribution
```bash
python -m src.pipeline --check-http-status
```
If 403 Forbidden or 429 Too Many Requests exceed 5%:

### 2. Inspect Proxy Gateway Ban Telemetry
```bash
curl -x http://proxy-gateway.internal:8080 -I https://boards.greenhouse.io
```

### 3. Step-by-Step Remediation
1. Rotate proxy session exit nodes to unbanned ASN ranges:
   ```bash
   python -m src.pipeline --rotate-proxy-pool
   ```
2. Increase human behavior delay jitter in scraper settings:
   ```python
   # In src/scraper_config.py
   MIN_DELAY_SECONDS = 3.5
   MAX_DELAY_SECONDS = 8.0
   ```
