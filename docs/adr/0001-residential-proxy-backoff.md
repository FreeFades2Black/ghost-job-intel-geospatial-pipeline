# ADR-0001: Rotating Residential Proxy Pools with Randomized Jitter vs Datacenter IPs

**Status:** Accepted  
**Date:** 2026-06-05  
**Lead Architect:** William Free Hall (Free) <whall4.wh@gmail.com>

## 1. Context & Operational Challenge
Scraping job vacancy telemetry across applicant tracking systems (Greenhouse, Lever, Workday, Indeed) to identify "ghost jobs" encounters strict Cloudflare and Akamai bot mitigation firewalls. Datacenter IP ranges (AWS, DigitalOcean) are blocked instantly with 403 Forbidden.

## 2. Options Considered
* **Option A: Datacenter Proxy Services with Headless Puppeteer**
  - *Evaluation:* Inexpensive, but subnet bans occur within minutes; TLS fingerprinting detects headless Chrome instantly.
* **Option B: Rotating Residential Proxy Pool with Realistic JA3/TLS Fingerprints and Exponential Jitter**
  - *Evaluation:* Rotates through residential ISP IPs per request session; mimics real browser TLS client hellos; jitter intervals (2-7 seconds) prevent rate-limit tripwires.

## 3. Decision & Trade-Off Accepted
We adopted **Option B (Rotating Residential Proxies)**.  
**Trade-Off Accepted:** Cost per GB bandwidth is higher (~$3.50/GB); request latency increases by ~400ms due to residential proxy routing hops.
