### What does np.array() do?

Converts an existing Python sequence (such as a list or tuple) or nested collection into a NumPy ndarray.

### What does np.zeros() create?

Creates a new array filled entirely with zeros (defaulting to float values) of a specified shape.

### What does np.ones() create?

Creates a new array filled entirely with ones (defaulting to float values) of a specified shape.

### What does np.full() do?

Initializes an array of a specified shape where every element is filled with a constant, predefined value (e.g., np.full((2, 3), 7)).

### What is the purpose of np.arange()?

Generates an array of evenly spaced values within a half-open interval [start, stop) based on a specified step size.

### What is the purpose of np.linspace()?

Generates an array of a specified number of evenly spaced points over a specified closed interval [start, stop].

### What is the difference between arange() and linspace()?

np.arange() determines array size by spacing (step), and the endpoint is generally excluded. np.linspace() determines spacing by the exact number of elements (num), and the endpoint is included by default.

### What is dtype?

The data type attribute of a NumPy array that dictates how the underlying binary data in memory is interpreted (e.g., int32, float64, bool).

### Why might float32 be preferable to float64 in some applications?

float32 consumes half the memory per element compared to float64. This reduces memory bandwidth bottlenecks, speeds up calculations on GPUs/hardware accelerators, and allows larger batches or models to fit into limited RAM during machine learning and deep learning workloads.

### Why is reproducibility important when generating random data?

Setting a seed ensures that pseudo-random operations produce identical outputs across runs. This is critical for debugging, unit testing, validating scientific experiments, and achieving consistent results when training and splitting datasets in machine learning.