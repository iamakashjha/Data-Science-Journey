import numpy as np

marks = np.random.default_rng(42).integers(
    0, 101,
    size=(10, 5)
)

print("Marks Dataset:")
print(marks)

print("\nMarks Dataset Analysis")
print("----------------")
print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Total elements:", marks.size)
print("Number of students:", marks.shape[0])
print("Number of subjects:", marks.shape[1])
