import numpy as np

from implementation import KMeans

X = np.array([
    [1.0, 1.0],
    [1.5, 2.0],
    [2.0, 1.5],
    [2.5, 2.0],
    [8.0, 8.0],
    [8.5, 9.0],
    [9.0, 8.5],
    [9.5, 9.0],
    [4.0, 8.0],
    [4.5, 9.0],
    [5.0, 8.5],
    [5.5, 9.0],
])

model = KMeans(n_clusters=3, max_iter=100, tol=1e-4, random_state=42)
labels = model.fit_predict(X)

print("Cluster labels:")
print(labels)
print("\nCluster centers:")
print(model.cluster_centers_)
print("\nInertia:", model.inertia_)

X_new = np.array([
    [2.0, 2.0],
    [9.0, 9.0],
    [5.0, 8.8],
])
print("\nPredictions for new data:")
print(model.predict(X_new))
