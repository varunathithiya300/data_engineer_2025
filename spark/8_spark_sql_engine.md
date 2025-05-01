#### Concepts through potential interview questions

1. What is `catalyst oprimizer / sql engine` ?
2. Why do we get `analysis exception error` ?
3. What is `catalog` ?
4. What is `physical planning / spark plan` ?
5. Is spark sql engine a compiler ?
   - `Yes` converts developer code to java byte code
6. How many phases are involved in spark sql engine to convert a code into java byte code ?

- SQL/Dataframe API/Dataset -> Catalyst Optimizer / Spark SQL Engine -> RDD (java byte code)

#### 4 Phases of Spark SQL Engine

- Analysis
- Logical planning
- Physical planning
- Code generation

#### Code execution plan

- `Developer Code`
- `Unresolved logical plan`
  |
  | Analysis <-- Catalog (metadata) --> `Analysis Exception Error`
  |
- `Resolved logical plan`
  |
  | Logical Optimization
  |
- `Optimized logical plan`
- `Physical plan` (multiple physical plans)
  |
  | cost-model
  |
- `Best physical plan` (set of RDDs) - > RDDs are sent to executors
- `Final RDD`
