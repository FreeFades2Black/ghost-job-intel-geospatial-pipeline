## Ghost Job Pipeline Operational Overview
*Describe modifications to ATS parsers, proxy rotation, or geospatial verification algorithms.*

- [ ] ATS Parser Module (Greenhouse, Lever, Workday)
- [ ] Anti-Bot Evasion & Proxy Pool Rotation
- [ ] Geospatial Density & Ghost Classification ($N \ge 30$)
- [ ] TimesFM Posting Velocity Model

## Safety & Anti-Scraping Verification
- **Rate Limit Compliance:** Verified requests per second do not exceed domain threshold (max 8 req/s).
- **Proxy Health Validated:** Confirmed session rotation functions without leaking origin IP.

## Verification Checklist
- [ ] Test suite passed (4/4 tests): `python -m pytest tests/ -v`
- [ ] Data files restored and clean
