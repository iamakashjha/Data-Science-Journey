import numpy as np
import timeit


# ============================================================
# 1. DTYPE
# ============================================================

numbers = np.array([10, 20, 30, 40, 50])

print("Dtype:", numbers.dtype)
print("Item size:", numbers.itemsize)
print("Number of elements:", numbers.size)
print("Memory:", numbers.nbytes)


# ============================================================
# 2. DIFFERENT DTYPES
# ============================================================

int8_array = np.array([10, 20, 30], dtype=np.int8)
int32_array = np.array([10, 20, 30], dtype=np.int32)
int64_array = np.array([10, 20, 30], dtype=np.int64)

print("\n--- Integer Memory ---")
print("int8:", int8_array.nbytes)
print("int32:", int32_array.nbytes)
print("int64:", int64_array.nbytes)


# ============================================================
# 3. LARGE ARRAYS
# ============================================================

float64_array = np.zeros(10_000_000, dtype=np.float64)
float32_array = np.zeros(10_000_000, dtype=np.float32)

print("\n--- Large Array Memory ---")
print("float64:", float64_array.nbytes)
print("float32:", float32_array.nbytes)


# ============================================================
# 4. VIEW VS COPY
# ============================================================

arr = np.array([10, 20, 30, 40, 50])
view = arr[1:4]
copy = arr[1:4].copy()

print("\n--- Memory Sharing ---")
print("arr and view:", np.shares_memory(arr, view))
print("arr and copy:", np.shares_memory(arr, copy))


# ============================================================
# 5. MODIFY VIEW
# ============================================================

view[0] = 999

print("\nOriginal after modifying view:")
print(arr)

print("\nView:")
print(view)

print("\nCopy:")
print(copy)


# ============================================================
# 6. MODIFY COPY
# ============================================================

copy[0] = 777

print("\nOriginal after modifying copy:")
print(arr)

print("\nCopy after modification:")
print(copy)


# ============================================================
# 7. ADVANCED INDEXING
# ============================================================

advanced = arr[[1, 2, 3]]

print("\nAdvanced indexing:")
print(advanced)
print("Shares memory:", np.shares_memory(arr, advanced))


# ============================================================
# 8. VECTOR PERFORMANCE
# ============================================================

python_code = """
result = []

for x in range(1_000_000):
    result.append(x * 2)
"""

numpy_code = """
result = np.arange(1_000_000) * 2
"""

python_time = timeit.timeit(python_code, number=5)
numpy_time = timeit.timeit(numpy_code, setup="import numpy as np", number=5)

print("\n--- Performance ---")
print("Python loop:", python_time)
print("NumPy:", numpy_time)


# ============================================================
# 9. ARRAY INFORMATION
# ============================================================

matrix = np.zeros((1000, 1000), dtype=np.float64)

print("\n--- Matrix Information ---")
print("Shape:", matrix.shape)
print("Size:", matrix.size)
print("Dtype:", matrix.dtype)
print("Itemsize:", matrix.itemsize)
print("Nbytes:", matrix.nbytes)


# ============================================================
# 10. IN-PLACE OPERATION
# ============================================================

values = np.array([1, 2, 3, 4, 5])
values *= 10

print("\nAfter in-place multiplication:")
print(values)
