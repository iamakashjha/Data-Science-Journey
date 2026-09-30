# Day 63 Exercises

## Exercise 1 — Fit

Create:

```python
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])
```

Create:

```python
pca = PCA(n_components=1)
```

Run:

```python
pca.fit(X)
```

Inspect:

```python
pca.mean_
pca.components_
pca.explained_variance_
```

---

## Exercise 2 — Transform

Transform:

```python
X_transformed = pca.transform(X)
```

Verify:

```python
X_transformed.shape
```

Expected:

```python
(5, 1)
```

---

## Exercise 3 — Inverse Transform

Run:

```python
X_reconstructed = pca.inverse_transform(X_transformed)
```

Compare:

```python
X
```

with:

```python
X_reconstructed
```

Calculate:

```python
mse = np.mean((X - X_reconstructed) ** 2)
```

---

## Exercise 4 — Test Data

Create:

```python
X_test = np.array([
    [6, 7],
    [7, 8],
    [8, 9]
])
```

Do:

```python
X_test_transformed = pca.transform(X_test)
```

Do not call:

```python
pca.fit(X_test)
```

Explain why.

---

## Exercise 5 — Whitening

Create:

```python
pca = PCA(n_components=2, whiten=True)
```

Run:

```python
X_white = pca.fit_transform(X)
```

Calculate:

```python
X_white.var(axis=0)
np.cov(X_white, rowvar=False)
```

Explain the result.

---

## Challenge

Improve the PCA class.

Add:

```python
def get_covariance(self):
    ...
```

It should return the covariance matrix learned during fit().

Store:

```python
self.covariance_
```

Then:

```python
pca.covariance_
```

should work.

---

## Bonus Challenge

Add a method:

```python
def reconstruction_error(self, X):
    ...
```

It should:

- transform X
- reconstruct X
- calculate MSE
- return the error

Example:

```python
error = pca.reconstruction_error(X)
```
