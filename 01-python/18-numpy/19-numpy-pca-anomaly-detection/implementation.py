import importlib.util
from pathlib import Path

import numpy as np


current_dir = Path(__file__).resolve().parent
pca_path = current_dir.parent / "17-numpy-pca-from-scratch" / "implementation.py"

spec = importlib.util.spec_from_file_location("pca_day63", pca_path)
pca_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pca_module)
PCA = pca_module.PCA


# ============================================================
# 1. CREATE NORMAL DATA
# ============================================================

rng = np.random.default_rng(42)

n_normal = 500

x = rng.normal(size=n_normal)
y = 2 * x + rng.normal(scale=0.2, size=n_normal)

X_normal = np.column_stack([x, y])


# ============================================================
# 2. CREATE ANOMALIES
# ============================================================

X_anomalies = np.array([
    [3, -6],
    [-4, 8],
    [5, 0],
    [-5, -1],
    [0, 8],
])


# ============================================================
# 3. COMBINE DATA
# ============================================================

X = np.vstack([X_normal, X_anomalies])

print("Normal Shape:")
print(X_normal.shape)

print("\nComplete Dataset Shape:")
print(X.shape)


# ============================================================
# 4. FIT PCA ON NORMAL DATA
# ============================================================

pca = PCA(n_components=1)
pca.fit(X_normal)


# ============================================================
# 5. CALCULATE TRAINING SCORES
# ============================================================

X_normal_reduced = pca.transform(X_normal)
X_normal_reconstructed = pca.inverse_transform(X_normal_reduced)

train_residuals = X_normal - X_normal_reconstructed
train_scores = np.sum(train_residuals ** 2, axis=1)


# ============================================================
# 6. SELECT THRESHOLD
# ============================================================

threshold = np.percentile(train_scores, 99)
print("\nAnomaly Threshold:")
print(threshold)


# ============================================================
# 7. TRANSFORM ALL DATA
# ============================================================

X_reduced = pca.transform(X)


# ============================================================
# 8. RECONSTRUCT ALL DATA
# ============================================================

X_reconstructed = pca.inverse_transform(X_reduced)


# ============================================================
# 9. CALCULATE SCORES
# ============================================================

residuals = X - X_reconstructed
anomaly_scores = np.sum(residuals ** 2, axis=1)


# ============================================================
# 10. FLAG ANOMALIES
# ============================================================

is_anomaly = anomaly_scores > threshold

print("\nAnomaly Scores:")
print(anomaly_scores)

print("\nAnomaly Flags:")
print(is_anomaly)


# ============================================================
# 11. INSPECT LAST FIVE OBSERVATIONS
# ============================================================

print("\nKnown Anomalies:")
print(X_anomalies)

print("\nScores for Known Anomalies:")
print(anomaly_scores[-len(X_anomalies):])

print("\nFlags for Known Anomalies:")
print(is_anomaly[-len(X_anomalies):])


# ============================================================
# 12. COUNT DETECTED ANOMALIES
# ============================================================

print("\nNumber of Flagged Observations:")
print(np.sum(is_anomaly))


# ============================================================
# 13. FALSE POSITIVE COUNT ON NORMAL DATA
# ============================================================

normal_flags = is_anomaly[:n_normal]
print("\nNormal Observations Flagged:")
print(np.sum(normal_flags))


# ============================================================
# 14. TRUE ANOMALY FLAGS
# ============================================================

known_anomaly_flags = is_anomaly[n_normal:]
print("\nKnown Anomalies Flagged:")
print(np.sum(known_anomaly_flags))
