
# RBC Application Monitoring Assignment

This repository contains solutions for TEST 1, TEST 2, and TEST 3 as requested.

--------------------------------------------------
TEST 1: Application & Service Monitoring (Python + FastAPI)
--------------------------------------------------

Application: rbcapp1  
Dependent services:
- httpd
- rabbitmq-server
- postgresql

Application status:
- UP   -> all services are UP
- DOWN -> any service is DOWN

### How to run TEST 1

1. Ensure Elasticsearch is running locally on port 9200
2. Install dependencies:
   pip install -r requirements.txt
3. Start FastAPI:
   uvicorn app.main:app --reload
4. Open Swagger UI:
   http://localhost:8000/docs

--------------------------------------------------
TEST 2: Ansible
--------------------------------------------------

Inventory defines three hosts running services independently.
Playbook supports:
- verify_install
- check-disk
- check-status (calls FastAPI endpoint)

--------------------------------------------------
TEST 3: CSV Processing
--------------------------------------------------

Python script filters properties sold below average price per square foot.

--------------------------------------------------
