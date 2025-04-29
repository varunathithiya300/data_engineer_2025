#### Concepts through potential interview questions

1. What is a transformation and how many types of transformation do we have ?
2. What happends when we use group by or join in a transformation ?
3. How are jobs created in spark ?

- A transformation is an operation that creates a new `RDD`, `Dataframe`, or `Dataset` from an existing one. Transformations are `lazily evaluated`. A transformation is executed only when an `action` is `triggered`.

- There are two types of transformation

  - `Narrow` dependency transformation -> `filter, select, union, map`
    - Transformations that does not require data movement between partitions.
  - `Wide` dependency transformation -> `join, groupby, distinct`
    - Transformation that require data movement between partitions - `shuffling`.
    - Shuffling -> data movement between data partitions

- Action -> count, show, collect
