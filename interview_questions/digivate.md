Role - Senior Data ENgineer
Org - Digivate Labs
Date - 27/05/2025

1. How to implement change data capture in a pipeline ?
2. What is the difference between a normalized view and materialized view ?
3. Data ingestion via Databricks Autoloader is is experiencing data skew. How to debug this ?
4. A small aggregation is taking a lot of time to complete in databricks. How will you troubleshoot ?
5. How will you plan the migration of data from an RDBMS to databricks ?

---

### **1. Change Data Capture (CDC)**

- **Concept:** Techniques to track and propagate only the changes (inserts, updates, deletes) in source data rather than full reloads.
- **Focus:** Data freshness, incremental processing, efficiency in ETL pipelines.

---

### **2. Normalized View vs Materialized View**

- **Concept:** Understanding of **data modeling** and **performance optimization**.

  - **Normalized View:** Logical representation using normalized tables (no data storage).
  - **Materialized View:** Precomputed, stored results for faster querying.

- **Focus:** Trade-offs between storage, performance, and data consistency.

---

### **3. Data Skew in Databricks Autoloader**

- **Concept:** **Skew handling and partitioning strategy** in distributed systems.
- **Focus:** Understanding of Spark internals—how data is distributed, shuffled, and processed across nodes. Debugging performance bottlenecks.

---

### **4. Performance Troubleshooting**

- **Concept:** **Spark performance tuning**.
- **Focus:** Root cause analysis—like small file problems, skew, broadcast joins, inefficient code, or cluster resource issues.

---

### **5. RDBMS to Databricks Migration**

- **Concept:** **Data migration strategy** and **architecture planning**.
- **Focus:** Schema mapping, data type conversion, batch vs incremental load, validation, and maintaining data integrity across systems.

---

These questions evaluate your **technical depth, practical experience, and system design thinking** as a data engineer.
