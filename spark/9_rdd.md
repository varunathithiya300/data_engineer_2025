#### Resilient Distributed Dataset

##### Concepts through potential interview questions

1. What is RDD ?

2. When do we need an RDD ?

   - Disadvantage

     - No optimization done by spark. Optimization responsibility lies with developer.
     - How to
     - Ease of use by developers

   - Advantage

     - Works well on structured data
     - Type safe (datatypes resolved during compile time)

   - Structured API
     - Dataframe API
     - Dataset API
     - rows and columns
     - keys and values

3. Features of an RDD -> Immutable, Lazy, Optimizations

4. What is dataframe / dataset?

   - Dataframe is a structued api
     - rows and columns
     - keys and values

5. Why shouldn't we use an RDD ?
   - RDD - how to do ?
   - Dataframe - what to do ?

**General points**

- `Resilient` -> In case of failure, automatically recovers
- `Distributed` -> Over the cluster
- `Dataset` -> Actual data
- `RDD` -> An immutable datastructure (once created, cannot be changed)
- `Advantage of immutability of RDD`
  - The RDD are connected through a DAG (Directed Acyclic Graph)
  - If any one of the RDD fails, the failed RDD will be restored by leveraging the logic stored in the DAG
