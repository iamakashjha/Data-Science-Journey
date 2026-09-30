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
# CREATE DATASET
# ============================================================

rng = np.random.default_rng(42)

n_samples = 500

feature_1 = rng.normal(size=n_samples)
feature_2 = feature_1 * 0.8 + rng.normal(scale=0.3, size=n_samples)
feature_3 = feature_1 * 0.5 + rng.normal(scale=0.4, size=n_samples)
feature_4 = rng.normal(size=n_samples)
feature_5 = feature_4 * 0.7 + rng.normal(scale=0.2, size=n_samples)
feature_6 = rng.normal(size=n_samples)

X = np.column_stack([
    feature_1,
    feature_2,
    feature_3,
    feature_4,
    feature_5,
    feature_6
])

print("Original Shape:")
print(X.shape)


# ============================================================
# FIT FULL PCA
# ============================================================

pca = PCA()
pca.fit(X)

explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

print("\nExplained Variance Ratio:")
print(explained_variance)

print("\nCumulative Explained Variance:")
print(cumulative_variance)


# ============================================================
# FIND COMPONENT COUNT
# ============================================================

thresholds = [0.80, 0.90, 0.95, 0.99]
print("\nComponent Selection:")

for threshold in thresholds:
    n_components = np.searchsorted(cumulative_variance, threshold) + 1
    print(f"{threshold:.0%} variance → {n_components} components")


# ============================================================
# SELECT 90% VARIANCE
# ============================================================

threshold = 0.90
n_components = np.searchsorted(cumulative_variance, threshold) + 1
print(f"\nSelected Components for {threshold:.0%} variance:")
print(n_components)


# ============================================================
# TRANSFORM
# ============================================================

pca_reduced = PCA(n_components=n_components)
X_reduced = pca_reduced.fit_transform(X)

print("\nReduced Shape:")
print(X_reduced.shape)


# ============================================================
# COMPRESSION RATIO
# ============================================================

original_features = X.shape[1]
reduced_features = X_reduced.shape[1]
compression_ratio = reduced_features / original_features

print("\nCompression Ratio:")
print(compression_ratio)

print("\nFeature Reduction:")
print(f"{original_features} → {reduced_features}")


# ============================================================
# RECONSTRUCTION
# ============================================================

X_reconstructed = pca_reduced.inverse_transform(X_reduced)
reconstruction_error = np.mean((X - X_reconstructed) ** 2)

print("\nReconstruction MSE:")
print(reconstruction_error)


# ============================================================
# RETAINED VARIANCE
# ============================================================

retained_variance = pca_reduced.explained_variance_ratio_.sum()
print("\nActual Retained Variance:")
print(retained_variance)
