# CSC 101 Final Project — PM2.5 Air Quality Report

> **Note:** This repository contains a **school project** created for **CSC 101**. It is being shared publicly for portfolio/learning purposes.

[Watch our video overview here!](https://www.youtube.com/watch?v=loot2YOKKLk)

## Project Proposal

**Course:** CSC 101 (Final Project)  
**Authors:** Amir Vered & Tobias Braddock-Ortiz

---

## Dataset

**Fine Particles in Major CA Coastal Cities**  
PM2.5 readings from **September 2025 – January 2026** in:
- Los Angeles (LA)
- Mexicali
- Sacramento

---

## Problem Statement

Fine particulate matter—specifically **PM2.5**—is known to cause serious harm to human respiratory health. This project aims to:
- Bring awareness to current PM2.5 levels in heavily populated urban areas (common PM2.5 hotspots)
- Evaluate whether the measured levels align with health standards
- Help inform whether **personal actions** or broader **policy/government action** may be warranted based on the data

---

## Planned Class and Data Structure Design

### Central Class: `City`

#### Attributes
- `monthly_average`
- `weekly_average`
- `daily_average`
- `highest_value`, `highest_timestamp`
- `lowest_value`, `lowest_timestamp`
- `days_exceeding_standards`

#### Methods
- `average_monthly()` → PM2.5 in µg/m³ (LC)
- `average_weekly()` → PM2.5 in µg/m³ (LC)
- `average_daily()` → PM2.5 in µg/m³ (LC)
- `highest_recording()` → PM2.5 in µg/m³ (LC) + timestamp
- `lowest_recording()` → PM2.5 in µg/m³ (LC) + timestamp
- `days_exceeding_health_standards()` → list of timestamps

**Initialization plan:**  
All calculations will be performed during `__init__` when a `City` object is created. Then, `__repr__` will generate a clean, printable summary of the computed statistics.

#### Additional Report-Level Method
- `overall_average()` → PM2.5 in µg/m³ (LC)

This method will be used to generate a combined report when multiple cities are loaded.

---

## File Handling Plan

**Inputs:**  
- 3 CSV files (one per city)

**Processing:**  
- CSVs will be parsed and loaded into `City` objects

**Output:**  
- 1 generated `.txt` report file containing summaries and key insights after program completion

---

## Expected Outputs / Insights

The program will generate a **text-based summary report** containing:
- Key PM2.5 statistics for each city (daily/weekly/monthly averages)
- Highest and lowest recorded values with timestamps
- A list/count of days that exceed health standards
- Overall insights comparing pollution prevalence across the cities

**Goal:**  
Determine whether PM2.5 levels in major urban areas are within healthy standards. Ideally, the results indicate safe levels; if not, this project can help communicate risk and support calls to action.
