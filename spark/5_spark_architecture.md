1. `Cluster` - A group of computers connected over a network

**Scenario**

- Consider a cluster of `9 workers` and `1 driver` i.e., Total 10 computers
- 20 core per machine
- 100 GB Ram per machine
- Total cores = 20 x 10 = 200 cores
- Total RAM = 100 x 10 = 1000 GB or 1 TB
- The driver has a software installed called cluster manager i.e., YARN
- The worker has a software installed called node manager.

- When a developer creates a saprk application, the developer interacts with the cluster manager.
- The cluster manager then interacts with any random node in the cluster.
- This node is called the `application master container`

- Spark core understands only Java
- Developer writes the code in PySpark, R, Scala
- The `main()` of the high level languages are converted into main() method of `JVM` for the Spark core to understand.
- This JVM is called the `application driver`

- Developer -> Cluster Manager -> Application Master (pyspark method -> JVM method i.e., Application_driver) -> Master -> Cluster Manager -> Resources are allocated
