# ADR-0002: Spatial Density Quota (N >= 30) for Authentic Job Vacancy Classification

**Status:** Accepted  
**Date:** 2026-06-26  
**Lead Architect:** William Free Hall (Free) <whall4.wh@gmail.com>

## 1. Context & Operational Challenge
Many companies maintain phantom job postings indefinitely for brand visibility or talent pipelining without active hiring budgets. We needed a rigorous mathematical heuristic to flag unfulfilled postings as authentic versus ghost positions.

## 2. Options Considered
* **Option A: Pure Duration-Based Metric (e.g. Open > 90 Days)**
  - *Evaluation:* Flawed heuristic; specialized executive or technical clearance positions naturally take 90+ days to fill.
* **Option B: Geospatial Cluster Density ($N \ge 30$) with TimesFM Applicant Velocity Modeling**
  - *Evaluation:* Cross-references employer physical facility boundaries, local commuting zones (15-mile radius), and active application ingestion velocity; flags postings persisting with zero interviewing activity despite high local talent supply.

## 3. Decision & Trade-Off Accepted
We adopted **Option B (Spatial Density & Velocity)**.  
**Trade-Off Accepted:** Discards sparse rural postings with $N < 30$ samples to eliminate statistical noise; ensures reported ghost job indices maintain a 99% confidence interval.
