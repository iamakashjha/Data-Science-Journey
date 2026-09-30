# Day 61 — NumPy PCA Foundations

## Objective

Understand the mathematical foundations of Principal Component Analysis using NumPy.

## Topics

- Dimensionality reduction
- PCA
- Centering
- Covariance matrix
- Eigenvalues
- Eigenvectors
- Principal components
- Explained variance
- Cumulative explained variance
- Data projection
- SVD-based PCA
- Feature scaling

## Key Questions

1. What is PCA?
2. Why is dimensionality reduction useful?
3. Why do we center data?
4. What is a covariance matrix?
5. What is a principal component?
6. What do eigenvalues represent in PCA?
7. What do eigenvectors represent?
8. What is explained variance?
9. How is PCA connected to SVD?
10. Why can feature scaling matter for PCA?

## Machine Learning Connection

PCA is commonly used for:

- dimensionality reduction
- visualization
- feature extraction
- preprocessing
- noise reduction

The mathematical foundation connects directly to:

- covariance matrices
- eigenvalues
- eigenvectors
- SVD

---

## Day 61 Completion Checklist

- [ ] Created 15-numpy-pca-foundations
- [ ] Created all standard project files
- [ ] Understood dimensionality reduction
- [ ] Understood PCA
- [ ] Understood variance
- [ ] Understood covariance
- [ ] Centered a dataset
- [ ] Calculated a covariance matrix
- [ ] Used np.linalg.eigh()
- [ ] Sorted eigenvalues
- [ ] Sorted eigenvectors
- [ ] Calculated explained variance ratio
- [ ] Calculated cumulative explained variance
- [ ] Projected data onto principal components
- [ ] Understood PCA through SVD
- [ ] Used np.linalg.svd()
- [ ] Understood Vt in SVD-based PCA
- [ ] Understood why scaling can matter
- [ ] Completed the PCA challenge
- [ ] Answered the 5 interview questions
- [ ] Completed the reflection

## Where We Are Now

Your NumPy progression is now moving toward data reduction and feature extraction:

18-numpy/
├── 01-why-numpy
├── 02-array-creation
├── 03-dimensions-shape-size
├── 04-indexing-slicing
├── 05-array-operations-broadcasting
├── 06-aggregations-statistics
├── 07-random-reproducibility
├── 08-reshaping-stacking-splitting
├── 09-boolean-masking-filtering
├── 10-advanced-indexing-sorting-ranking
├── 11-end-to-end-numpy-analysis
├── 12-numpy-performance-memory-efficiency
├── 13-numpy-linear-algebra
├── 14-numpy-eigenvalues-decompositions
└── 15-numpy-pca-foundations   ← Day 61

The learning path now looks like:

NumPy Fundamentals
       ↓
Array Manipulation
       ↓
Data Analysis
       ↓
Advanced Indexing
       ↓
Performance
       ↓
Linear Algebra
       ↓
Eigenvalues / Eigenvectors
       ↓
SVD
       ↓
PCA
       ↓
Machine Learning

## Day 61 Core Takeaway

PCA transforms a dataset into a new set of orthogonal directions called principal components. The eigenvectors of the covariance matrix provide those directions, while the corresponding eigenvalues determine how much variance each component explains. SVD provides another powerful way to compute PCA.
