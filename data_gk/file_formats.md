| **Format** | **Type**             | **Best For**       | **Compression** | **Schema Support** | **Notes**                   |
| ---------- | -------------------- | ------------------ | --------------- | ------------------ | --------------------------- |
| `Parquet`  | Columnar             | Analytics          | Yes             | Yes                | Best for batch & lakehouses |
| `ORC`      | Columnar             | Hive, Presto       | Yes             | Yes                | Great compression           |
| `Arrow`    | Columnar (in-memory) | Fast interchange   | ⚠️ (in-memory)  | Yes                | Not for storage             |
| `Avro`     | Row-based            | Kafka, streaming   | Yes             | Yes                | Schema evolution            |
| `JSON`     | Semi-structured      | APIs, logs         | No              | ⚠️                 | Readable, but inefficient   |
| `Delta`    | Hybrid               | Lakehouse (ACID)   | Yes             | Yes                | Built on Parquet            |
| `Hudi`     | Hybrid               | CDC & streaming    | Yes             | Yes                | Incremental writes          |
| `Iceberg`  | Hybrid               | Cloud-native lakes | Yes             | Yes                | Multi-engine support        |
| `CSV`      | Text                 | Small data         | No              | No                 | Legacy/portable             |
