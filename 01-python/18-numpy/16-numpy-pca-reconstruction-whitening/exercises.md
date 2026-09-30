# Day 62 Exercises

## Exercise 1 — Reconstruction

Create a random dataset:

```python
rng = np.random.default_rng(42)
X = rng.normal(size=(200, 6))
```

Perform PCA.

Keep 2 components.

Reconstruct the original dataset.

Calculate:

```python
MSE = np.mean((X - X_reconstructed) ** 2)
```

---

## Exercise 2 — Compare Components

Perform reconstruction using:

- 1 component
- 2 components
- 3 components
- 4 components
- 5 components
- 6 components

Create a table:

```text
Components | Explained Variance | Reconstruction MSE
```

Observe the relationship.

---

## Exercise 3 — Reconstruction Quality

Write code that verifies:

```python
More components -> lower reconstruction error
```

Use:

```python
np.all(np.diff(errors) <= 0)
```

Be careful: tiny floating-point differences may require a tolerance-based comparison.

---

## Exercise 4 — Whitening

Take the first three principal components.

Create:

```python
X_white = X_reduced / np.sqrt(eigenvalues[:3] + 1e-8)
```

Then calculate:

```python
X_white.mean(axis=0)
X_white.var(axis=0)
```

What do you observe?

---

## Exercise 5 — Covariance After Whitening

Calculate:

```python
np.cov(X_white, rowvar=False)
```

Check whether the covariance matrix is approximately:

```python
np.eye(3)
```

Explain why.

---

## Challenge

Build a reusable class:

```python
class PCA:
    ...
```

with:

- fit(X)
- transform(X)
- fit_transform(X)
- inverse_transform(X)

Your class should store:

- mean_
- components_
- eigenvalues_
- explained_variance_ratio_

Example:

```python
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
X_reconstructed = pca.inverse_transform(X_reduced)
```

Calculate the reconstruction error.

---

## Bonus Challenge — Add Whitening

Extend your class:

```python
PCA(n_components=2, whiten=True)
```

Then:

```python
pca.fit_transform(X)
```

should return whitened principal-component scores.

Think carefully about where the whitening operation should happen.
