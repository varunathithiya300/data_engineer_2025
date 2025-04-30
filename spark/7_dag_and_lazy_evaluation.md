1. One spark job is spawned per action
2. Every spark job has a DAG
3. Filtering a.k.a. predicate pushdown, projection pruning
4. Spark UI
   - Available for every job created
   - Tabs available in Spark UI
     - Jobs -> Stages -> Storage -> Environment -> Executors -> SQL/DataFrame -> JDBC/ODBC Server -> Structured Streaming
5. Every code we write is optimized automatically (catalyst optimizer) because of lazy evaluation.
