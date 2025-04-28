1. Initially databases came into existence i.e., Oracle, Teradata, exadata, Mysql, Postgresql etc.

2. Databases were only capable to handle structured data. (rows + columns i.e., tabular format)

3. Boom of internet ->

   - `Variety` of data (structured, unstructured, semi-structured)
     - structured -> csv, .sql, .db, .xlsx, .xml
     - semistructured -> json, yaml, email, log, iot, nosql
     - unstructured -> .txt, .docx, .pdf, images, audio, video
   - `Volume` of data (GB, TB, PB)
   - `Velocity` of data (per unit time)
   - All the three characteristics (3V) together is called `Big Data`
   - The need for some technology was realized -> `Hadoop` -> `Apache Spark`

4. ETL - Extract Transform Load (traditional)

5. ELT - Extract Load Transform (modern)

6. Big Data bottlenecks

   - Storage
   - Processing (RAM, CPU)

7. Two approaches to solve #6

   - `Monolithic Approach` (can only be scaled vertically -> real estate shortage, heat generation, cost exponentially increases due to hw/sw updates)
   - `Distributed Approach` (can be scaled horizontally, economical, high availability)

8. First contender to solve the Big Data - `Hadoop`
9. Successor to hadoop - `Apache Spark`
