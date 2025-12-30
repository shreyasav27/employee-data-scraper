# Employee Data Scraper

## Overview
This project fetches employee data from a public API, processes and normalizes the data, and generates a clean CSV file ready for ingestion into a database or data warehouse.

## Features
- Fetches employee data using REST API
- Handles API errors and timeouts gracefully
- Normalizes employee data
- Creates full name and designation columns
- Validates phone numbers
- Ensures correct data types
- Handles missing fields safely
- Outputs clean CSV file

## Tech Stack
- Python
- Requests
- Pandas

## How to Run
```bash
pip install requests pandas
python employee_scrapper.py
