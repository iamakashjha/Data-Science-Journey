import numpy as np


def memory_report(array):
    print("========================================")
    print("NUMPY ARRAY MEMORY REPORT")
    print("========================================")
    print("Shape:", array.shape)
    print("Dimensions:", array.ndim)
    print("Elements:", array.size)
    print("Dtype:", array.dtype)
    print("Bytes per element:", array.itemsize)
    print("Total bytes:", array.nbytes)
    print("Total KB:", array.nbytes / 1024)
    print("Total MB:", array.nbytes / (1024 ** 2))


# Example usage
if __name__ == "__main__":
    a = np.zeros((2000, 2000), dtype=np.float64)
    b = np.zeros((2000, 2000), dtype=np.float32)

    print("\n--- float64 ---")
    memory_report(a)

    print("\n--- float32 ---")
    memory_report(b)


# Advanced challenge

def compare_dtypes(shape):
    float32_array = np.zeros(shape, dtype=np.float32)
    float64_array = np.zeros(shape, dtype=np.float64)

    print("float32 dtype:", float32_array.dtype)
    print("float32 memory:", float32_array.nbytes)
    print("float64 dtype:", float64_array.dtype)
    print("float64 memory:", float64_array.nbytes)
    print("Memory saved by float32:", float64_array.nbytes - float32_array.nbytes)


# Example
if __name__ == "__main__":
    compare_dtypes((10_000_000,))
