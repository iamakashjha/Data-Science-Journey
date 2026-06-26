## Reflection Questions

### 1. What is an eigenvector?

An eigenvector is a non-zero vector that, after a matrix transformation, keeps the same direction. It may only be stretched, compressed, or flipped.

### 2. What is an eigenvalue?

An eigenvalue is the scalar that tells **how much the corresponding eigenvector is scaled** during the transformation.

- Eigenvalue > 1: vector is stretched.
- Eigenvalue between 0 and 1: vector is compressed.
- Negative eigenvalue: vector flips direction.

### 3. Why doesn't an eigenvector change direction?

An eigenvector lies along a **special direction** of the transformation. When the matrix is applied, the vector is only multiplied by its eigenvalue, so its direction remains the same (or reverses if the eigenvalue is negative).

### 4. Why are eigenvalues useful?

Eigenvalues help identify the **most important directions and amount of variation** in data. They are useful for:

- Dimensionality reduction
- Understanding data variance
- Solving systems of equations
- Stability analysis
- Optimizing machine learning algorithms

### 5. Where might Data Scientists use eigenvectors?

Data Scientists use eigenvectors in many areas, including:

- **Principal Component Analysis (PCA)** for dimensionality reduction.
- Feature extraction and data compression.
- Image processing and facial recognition.
- Recommendation systems.
- Spectral clustering and graph analysis.

Eigenvectors identify the most informative directions in the data, while eigenvalues indicate how important each direction is.