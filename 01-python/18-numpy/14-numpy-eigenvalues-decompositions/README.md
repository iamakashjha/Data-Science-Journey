# Day 60 — NumPy Eigenvalues & Decompositions

## Objective

Understand eigenvalues, eigenvectors and SVD as important linear algebra tools for Data Science.

## Topics

- Eigenvalues
- Eigenvectors
- np.linalg.eig()
- Eigenvector verification
- Determinant relationship
- Matrix decomposition
- Singular Value Decomposition
- np.linalg.svd()
- Singular values
- Orthogonal matrices
- Low-rank approximation
- PCA connection

## Key Questions

1. What is an eigenvector?
2. What is an eigenvalue?
3. What does Av = λv mean?
4. How do you calculate eigenvalues in NumPy?
5. How do you verify an eigenvector?
6. What is SVD?
7. What are U, Σ and Vᵀ?
8. Why is SVD useful?
9. What is low-rank approximation?
10. How does SVD connect to PCA?

## Machine Learning Connection

Eigenvalues and eigenvectors are important mathematical components of PCA.

SVD is widely used for dimensionality reduction, matrix approximation and latent feature extraction.

---

## Day 60 Completion Checklist

- [ ] Created 14-numpy-eigenvalues-decompositions
- [ ] Created all standard project files
- [ ] Understand eigenvectors
- [ ] Understand eigenvalues
- [ ] Understand Av = λv
- [ ] Used np.linalg.eig()
- [ ] Verified eigenvectors
- [ ] Used np.allclose()
- [ ] Connected eigenvalues with determinants
- [ ] Understand matrix decomposition
- [ ] Understand SVD
- [ ] Used np.linalg.svd()
- [ ] Understand U, S, and Vt
- [ ] Reconstructed a matrix from SVD
- [ ] Understand singular values
- [ ] Built a low-rank approximation
- [ ] Understand orthogonality
- [ ] Connected SVD to dimensionality reduction
- [ ] Previewed the connection to PCA
- [ ] Completed the matrix-analysis challenge
- [ ] Answered the 5 interview questions
- [ ] Completed the reflection

## Where We Are Now

Your NumPy progression is becoming much more mathematically useful:

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
│
└── 14-numpy-eigenvalues-decompositions   ← Day 60

And the learning path is now:

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

## Day 60 Core Takeaway

Eigenvalues and eigenvectors help us understand important directions in matrix transformations, while SVD gives us a powerful way to decompose and approximate matrices. These concepts form an important mathematical bridge between NumPy and techniques such as PCA, dimensionality reduction, and Machine Learning.
