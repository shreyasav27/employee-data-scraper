# Employee Data Scraper

## Overview
This project fetches employee data from a public REST API, processes and normalizes the data, and generates a clean CSV file that is ready for ingestion into a database or data warehouse.

## Features
- Fetches employee data using a REST API  
- Handles API errors and request timeouts gracefully  
- Normalizes raw employee data  
- Creates **Full Name** and **Designation** columns  
- Validates phone numbers  
- Ensures correct data types  
- Safely handles missing or null fields  
- Exports the processed data to a clean CSV file  

## Tech Stack
- Python  
- Requests  
- Pandas  


## How to Run
```bash
pip install requests pandas
python employee_scrapper.py
This change is added to enable pull request creation

