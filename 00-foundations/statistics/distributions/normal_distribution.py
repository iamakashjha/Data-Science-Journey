import numpy as np

data = np.random.normal(
    loc=50,
    scale=10,
    size=100
)

print(data[:10])
print("Mean:", np.mean(data))
print("Std:", np.std(data))