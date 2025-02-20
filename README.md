# QuantFlux: Modular API Data Pipeline

## Overview
QuantFlux ingests structured API data, processes it using Airbyte, and loads it into Snowflake Iceberg. The goal is to establish a minimal but scalable pipeline while ensuring real-world applicability.

## Setup Instructions
1. Clone the repository: `git clone <repo-url>`
2. Navigate to the project directory: `cd QuantFlux`
3. Create a development branch: `git checkout -b dev`
4. Run the setup script: `bash setup.sh`
5. Install Airbyte (https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart) and Airflow (https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)


# **Project Plan: S&P 500 Data Pipeline (PoC → MVP)**
## **1. Overview**
### **1.1. Project Summary**
We aim to build a **scalable and extensible data pipeline** to ingest, store, and process **daily S&P 500 market data** from **Alpha Vantage**. The data will be partitioned by day and stored in **Snowflake Iceberg (Open Catalog)** for analytical use. This **PoC** (Proof of Concept) will evolve into an **MVP** (Minimum Viable Product) with future enhancements, such as backfilling historical data, integrating additional financial metrics (market cap, dividends), and eventual **integration with a trading platform**.

### **1.2. Goals**
- **Develop a quick PoC** that extracts S&P 500 data and loads it into a structured Iceberg table.
- **Ensure efficient data ingestion and partitioning** to optimize query performance.
- **Implement observability and logging** for tracking failures and ingestion success.
- **Enable future extensibility** for historical backfilling and trading platform integration.

---

## **2. Architecture**
### **2.1. Tech Stack**
| Component      | Technology Stack |
|---------------|----------------|
| **Orchestration** | Apache Airflow |
| **ETL Extraction** | Airbyte |
| **Data API** | Alpha Vantage (free tier) |
| **Storage & Processing** | Snowflake Iceberg (Open Catalog) |
| **Containerization** | Docker (local), Snowpark Containers (future) |
| **Logging & Monitoring** | Airflow logs, Snowflake query history |
| **Version Control** | GitHub |

### **2.2. Pipeline Workflow**
Airflow DAG → Airbyte API Extraction → Snowflake Iceberg (Bronze) → Logging & Monitoring
1. **Airflow schedules & triggers** the pipeline daily.
2. **Airbyte fetches S&P 500 data** from Alpha Vantage API.
3. **Data is loaded into Snowflake Iceberg**, partitioned by date.
4. **Logging & error tracking** captures ingestion success/failure.

---

## **3. Milestones & Phases**
### **Phase 1: Proof of Concept (PoC)**
✅ **Goal:** Ingest S&P 500 data for **one day** into Snowflake Iceberg.

- [ ] **Set up API connection** (Alpha Vantage API Key Management)
- [ ] **Develop Airbyte source connector** for data extraction
- [ ] **Create Snowflake Iceberg schema** (based on repo structure)
- [ ] **Implement Airflow DAG** to orchestrate ingestion
- [ ] **Load one day's data into Snowflake Iceberg (Bronze)**
- [ ] **Implement logging & failure handling** (Airflow logs, Snowflake monitoring)
- [ ] **Validate schema and data quality** (minimal checks)

### **Phase 2: Extend to MVP**
✅ **Goal:** Automate **daily ingestion** and enable **historical backfill**.

- [ ] **Implement daily scheduled ingestion**
- [ ] **Design & test backfill process** (1 year of historical data)
- [ ] **Optimize partitioning strategy** for efficient querying
- [ ] **Improve logging & monitoring** with structured alerts
- [ ] **Containerize pipeline** (Docker locally, plan for Snowpark Containers)
- [ ] **Validate scalability** under larger historical loads

### **Phase 3: Enhancements & Future Considerations**
✅ **Goal:** Expand functionality and optimize performance.

- [ ] **Add more financial metrics** (Market Cap, Dividend Yield)
- [ ] **Improve performance with batch processing** in Snowflake
- [ ] **Evaluate switching from Alpha Vantage to a more robust API**
- [ ] **Plan for trading platform integration** (Optional)
- [ ] **Migrate to managed container service** (Snowpark, Kubernetes, etc.)

---

## **4. Engineering Considerations**
### **4.1. Data Quality & Governance**
- **Minimal enforcement at Bronze layer**
- **Logging first, validation later** (data quality in later transformations)
- **Hash fingerprinting in future stages** (to detect duplicates/anomalies)

### **4.2. Scalability & Performance**
- **Daily partitioning strategy** ensures efficient time-series queries.
- **Backfill process must be idempotent** (no duplicate data issues).
- **Batch inserts over row-by-row ingestion** to optimize Snowflake performance.

### **4.3. Security & API Limits**
- **API Rate Limiting:** Implement retries/exponential backoff in case of failures.
- **API Key Management:** Store keys securely using environment variables.
- **Access Controls:** Limit Snowflake permissions to necessary roles.

---

## **5. Risks & Mitigations**
| Risk | Mitigation |
|------|-----------|
| **API limits may block backfill** | Implement batching & retry logic |
| **Schema evolution in API** | Introduce schema versioning checks |
| **Data integrity issues** | Implement fingerprinting in Silver layer |
| **Scaling ingestion for historical data** | Optimize batch size & parallelization |

---

## **6. Long-Term Vision**
- **Short-term:** Establish a stable ingestion pipeline for S&P 500 data.
- **Medium-term:** Expand dataset with market cap, dividends, and financial indicators.
- **Long-term:** Integrate with trading platforms, backtest direct indexing strategies.

---

## **7. Next Steps**
1. **Kickstart PoC**: Set up API access, Airflow, and Airbyte.
2. **Implement initial pipeline**: Load 1 day’s data into Snowflake Iceberg.
3. **Validate performance & logging**: Ensure ingestion is stable.
4. **Iterate towards MVP**: Automate daily loads and enable backfilling.
