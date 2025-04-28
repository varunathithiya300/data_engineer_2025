**Misconception**

- Hadoop is a database
- Spark is 100 times faster than Hadoop
- Spark processed data in RAM but Hadoop does not

**Comparison** - Performance, Processing type, Easy of use, Security, Fault tolerance

- `Performance`

  - Eventhough hadoop has a RAM, the results and always written to a disk. - Everytime, we need to process data, we have to read it from the disk. - A small `timedelta` is involved for every read/scan plus the processing time.
  - These time deltas accumulate to become a sizeable amount in the cases of higher workloads (AI, ML).
  - Hence, hadoop is slower than Spark where all the results are stored in the RAM.
  - Hadoop was invented by `Google` using the `Map Reduce`
  - Hadoop was designed to write to disk because, back in ~2004, the cost of RAM was very high. Also, the creators of Hadoop felt it was safer to write it to a disk so that the results could be accessed later.

- `Type of process` -> Batch & Stream

  - Hadoop was built for batch processing while Spark was built for batch + stream processing

- `Ease of use`

  - Difficult to write code in hadoop -> Hive was built later to fix this
  - Easy to write code. Different languages support (python, scala, sql)
    - high level api
    - low level api

- `Security`

  - Hadoop -> Kerberos (YARN) + ACL
  - Spark -> No exclusive security feature
    - Leverages ACL from HDFS
    - Kerberos from YARN

- `Fault Tolerance`
  - Hadoop - data is replicated across nodes with a replication factor
    - replication factor (default = 3) -> Number of instances where data is stored
    - partition size (default = 128 mb)
  - Spark
    - leverages RDD (Resilient Distributed Dataset). RDD is immutable
    - RDD is connected through a DAG (Directed Acyclic Graph)
    - In the event of failure, process is re-invoked from the corresponding DAG
