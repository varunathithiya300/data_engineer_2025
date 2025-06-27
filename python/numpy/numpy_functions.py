import numpy as np

# ## 1. **Array Creation**

# | Function              | Purpose                      | Example                            |
# | --------------------- | ---------------------------- | ---------------------------------- |
# | `np.array()`          | Create array from list/tuple | `np.array([1, 2, 3])`              |
# | `np.zeros()`          | Array of all 0s              | `np.zeros((2, 3))`                 |
# | `np.ones()`           | Array of all 1s              | `np.ones((3,))`                    |
# | `np.full()`           | Array with constant value    | `np.full((2, 2), 7)`               |
# | `np.arange()`         | Range of values              | `np.arange(0, 10, 2)`              |
# | `np.linspace()`       | Evenly spaced numbers        | `np.linspace(0, 1, 5)`             |
# | `np.eye()`            | Identity matrix              | `np.eye(3)`                        |
# | `np.random.rand()`    | Random values (0–1)          | `np.random.rand(2, 2)`             |
# | `np.random.randint()` | Random integers              | `np.random.randint(0, 10, (3, 3))` |

a = np.array([1, 2, 3])
b = np.zeros((2, 3), dtype=int)
c = np.ones((3,))
d = np.full((2, 2), 7)
e = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
f = np.arange(start=2, stop=9, step=0.5, dtype=int)
g = np.linspace(0, 1, 5)
h = np.eye(3, 3)
# i = np.random.rand(2,2, dtype=int)
i = np.random.randint(0, 5)
print(i)


# ## 2. **Array Attributes**

# | Attribute | Meaning                  | Example     |
# | --------- | ------------------------ | ----------- |
# | `.shape`  | Dimensions               | `arr.shape` |
# | `.ndim`   | Number of dimensions     | `arr.ndim`  |
# | `.dtype`  | Data type                | `arr.dtype` |
# | `.size`   | Total number of elements | `arr.size`  |

# ---

# ## 3. **Indexing and Slicing**

# | Task               | Function/Example   |
# | ------------------ | ------------------ |
# | Slice rows/columns | `arr[1:3, :]`      |
# | Boolean indexing   | `arr[arr > 5]`     |
# | Fancy indexing     | `arr[[0, 2]]`      |
# | Modify values      | `arr[arr < 0] = 0` |

# ---

# ## 4. **Math Operations**

# | Operation               | Function                  |
# | ----------------------- | ------------------------- |
# | Element-wise add        | `arr1 + arr2`             |
# | Multiply (element-wise) | `arr1 * arr2`             |
# | Dot product             | `np.dot(a, b)` or `a @ b` |
# | Exponentiation          | `np.exp(arr)`             |
# | Square root             | `np.sqrt(arr)`            |
# | Logarithm               | `np.log(arr)`             |

# ---

# ## 5. **Aggregation Functions**

# | Function                      | Purpose               | Example               |
# | ----------------------------- | --------------------- | --------------------- |
# | `np.sum()`                    | Sum of all/along axis | `np.sum(arr, axis=0)` |
# | `np.mean()`                   | Mean                  | `np.mean(arr)`        |
# | `np.median()`                 | Median                | `np.median(arr)`      |
# | `np.std()`                    | Standard deviation    | `np.std(arr)`         |
# | `np.min()` / `np.max()`       | Minimum / Maximum     | `np.min(arr)`         |
# | `np.argmax()` / `np.argmin()` | Index of max/min      | `np.argmax(arr)`      |

# ---

# ## 6. **Reshaping and Stacking**

# | Function                      | Purpose                       | Example                      |
# | ----------------------------- | ----------------------------- | ---------------------------- |
# | `np.reshape()`                | Change shape                  | `arr.reshape(3, 2)`          |
# | `np.ravel()`                  | Flatten                       | `arr.ravel()`                |
# | `np.flatten()`                | Flatten (copy)                | `arr.flatten()`              |
# | `np.transpose()`              | Swap axes                     | `arr.T` or `arr.transpose()` |
# | `np.vstack()` / `np.hstack()` | Stack vertically/horizontally | `np.vstack([a, b])`          |

# ---

# ## 7. **Sorting and Searching**

# | Function       | Purpose           | Example              |
# | -------------- | ----------------- | -------------------- |
# | `np.sort()`    | Sort array        | `np.sort(arr)`       |
# | `np.argsort()` | Indices of sorted | `np.argsort(arr)`    |
# | `np.where()`   | Conditional index | `np.where(arr > 10)` |
# | `np.unique()`  | Unique elements   | `np.unique(arr)`     |

# ---

# ## 8. **Handling NaNs**

# | Function             | Purpose             |
# | -------------------- | ------------------- |
# | `np.isnan(arr)`      | Detect NaNs         |
# | `np.nan_to_num(arr)` | Replace NaNs with 0 |
# | `np.nansum(arr)`     | Sum ignoring NaNs   |
# | `np.nanmean(arr)`    | Mean ignoring NaNs  |

# ---

# ## 9. **Linear Algebra (Optional Advanced)**

# | Function            | Purpose             |
# | ------------------- | ------------------- |
# | `np.linalg.inv()`   | Inverse of matrix   |
# | `np.linalg.det()`   | Determinant         |
# | `np.linalg.eig()`   | Eigenvalues/vectors |
# | `np.linalg.solve()` | Solve linear system |

# ---
