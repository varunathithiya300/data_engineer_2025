#### Concepts through potential interview questions

1. What is a `job`, `stage`, `task`, `application` in spark ?
2. How many jobs will be created in the given script ? (interviewer may give a code snipppet)
3. How many stages will be created ?
4. How many tasks will be created ?

- **General**
- One application can have many jobs
- One job can have many stages
- One stage can have many tasks
- A Spark application will always have at least one stage and at least one task, no matter how simple the job is.

- **Definitions**
- `Application` = A program that consists of a `driver` process and a set of `executor` processes, cooordinated to `complete a set of jobs`.

- `Job` = A job corresponds to an action. Each jon is broken into one or more stages

- `Stage` = A set of tasks that can be executed in parallel without a shuffle.

- `Shuffle` - read/write from different nodes in a cluster. A shuffle is determined by the nature of transformation. Narrow Dependency Transformation - No shuffle, Wide Dependency Transformation = Shuffle happens

- `Task` = Individual units of work sent to executors for processing

- `Driver` = The main process that runs the spark code, coordinates jobs and stages

- `Executors` = Worker processes that run tasks and store data across the cluster

- `Read exchange/write exchange`
