A faster internet connection can enhance the performance of a Spark application by delivering quicker results. However, since high-speed internet isn't always accessible, it's essential to optimize Spark applications through thoughtful code and configuration choices.

**Areas of improvement**

1. code-level design choices (RDDs vs DataFrames)
2. Data at rest
3. Joins
4. Aggregations
5. Data in flight
6. Individual application properties
7. DInside of JVM of an executor
8. Worker nodes
9. Cluster and deployment properties

**Direct approach**

1. `Scala vs Java vs Python vs R`
   Python widely used by many. Although preference is based on use case / client preference. However, it is better to write UDF in Java or Scala to reduce the performance hit.

2. `DataFrames vs SQL vs Datasets vs RDDs`
   RDD - Java or Scala
   Others - Python

3. `Cluster/application sizing and sharing`

   - A mechanism to dynamically adjust resources.
   - Application returns resources when not used and requests resources when in need
   - Disabled by default
   - Available on all coarse grained cluster managers - `standalone mode`, `YARN mode`, `Mesos coarse-grained mode`
   - `spark.dynamicAllocation.enabled` -> true

4. Scheduling

5. Data at rest
   File-based long-term data storage
   Splittable file types and compression
   Table partitioning
   Bucketing
   The number of files
   Data locality
   Statistics collection

6. Shuffle configurations
7. Memory pressure and garbage collection
   Measuring the impact of garbage collection
   Garbage collection tuning

**Direct Performance Enhancements**

1. Parallelism
2. Improved filtering
3. Repartitioning and coalescing
4. User-Defined Functions
5. Temporary data storage (caching)
   Reuse the same datasets over and over
   Caching incures a serialization, deserialization and storage

6. Joins

   - use equi joins wherever possible
   - avoid cartesian join or full outer join
   - predicate pushdown before joins
   - broadcast joins
   - bucketing (good to have)

7. Aggregations
   If using RDD reduceByKey groupByKey
8. Broadcast variables
9.
