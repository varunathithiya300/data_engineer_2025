1. What is repartition ?
2. What is coalesce ?
3. Which one will you choose and why ?
4. Repartitioning vs coalesce ?
5. What will happen when the number of partitions > number of records ?

- `Repartition` = df.repartition(n, column_name) -> n = 200 (default)

  - Pros = Even distribution of data.
  - Cons = More I/O. Expensive
  - Repartition can increase or decrease the number of partitions. (generally used to increase the partitions)
  - `df.rdd.getNumPartitions()` = To get the number of partitions
  - from pyspark.sql.functions import spark_partition_id -> `spark_partition_id`

- `Coalesce` = df.coalesce(n)

  - Pros - Not expensive
  - Con - Uneven distribution of data
  - Coalesce can only reduce the number of partitions
