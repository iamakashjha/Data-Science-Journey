# Day 64 Exercises

## Exercise 1 — Cumulative Variance

Given:

```python
variance_ratio = np.array([
    0.50,
    0.25,
    0.12,
    0.08,
    0.05
])
```

Calculate:

```python
np.cumsum(variance_ratio)
```

What percentage is retained by the first:

- 1 component?
- 2 components?
- 3 components?
- 4 components?
- 5 components?

---

## Exercise 2 — Threshold Selection

Using:

```python
variance_ratio = np.array([
    0.50,
    0.25,
    0.12,
    0.08,
    0.05
])
```

Find the minimum number of components needed to retain:

- 80%
- 90%
- 95%

Use:

```python
np.searchsorted()
```

Do not manually count them.

---

## Exercise 3 — Compression

Suppose:

```python
Original features = 500
PCA components = 50
```

Calculate:

- compression ratio
- dimensionality reduction percentage

---

## Exercise 4 — Reconstruction Error

Generate:

```python
rng = np.random.default_rng(42)
X = rng.normal(size=(1000, 20))
```

Fit PCA with:

- 5 components
- 10 components
- 15 components
- 20 components

For each:

1. transform
2. inverse transform
3. calculate MSE

Create:

```text
components → reconstruction error
```

Observe the relationship.

---

## Exercise 5 — PCA Loadings

Fit PCA with:

```python
n_components = 3
```

Inspect:

```python
pca.components_
```

For each component:

1. calculate absolute loadings
2. sort them
3. identify the top 3 contributing features

---

## Challenge

Build this function:

```python
def select_components(explained_variance_ratio, threshold):
    ...
```

Example:

```python
variance_ratio = np.array([
    0.45,
    0.25,
    0.15,
    0.10,
    0.05
])

n = select_components(variance_ratio, 0.90)
```

Expected:

```python
4
```

Your function should:

1. calculate cumulative variance
2. find the first component meeting the threshold
3. return the component count

Also validate:

```python
threshold > 0
threshold <= 1
```

---

## Bonus Challenge

Create:

```python
def pca_summary(pca):
    ...
```

It should return:

```python
Component
Explained Variance
Explained Variance Ratio
Cumulative Variance
```

For example:

```text
PC1    4.21    0.51    0.51
PC2    2.10    0.25    0.76
PC3    1.01    0.12    0.88
PC4    0.72    0.08    0.96
```
