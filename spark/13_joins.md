1. Shuffling is a process where the data having the same key is brought to the same executor. As a result, there is a lot of data moving across executors.

#### **Join Strategies**

1. Shuffle sort-merge join

   - Datasets are sorted based on the join key
   - Time complexity - `O(nlogn)`
   - CPU is getting utilised

2. Shuffle hash join

   - The hash of the smaller table is created `in memory`
   - Time complexity - O(1)

3. Broadcast hash join

4. Cartestian join

5. Broadcase nested loop join (most expensive O(n)^2)
