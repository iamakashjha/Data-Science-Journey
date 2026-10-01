# Day 65 Exercises

## Exercise 1 — Reconstruction Scores

Create:

```python
rng = np.random.default_rng(42)
X = rng.normal(size=(100, 5))
```

Fit PCA with:

```python
2 components
```

Calculate:

```python
reconstruction_score = np.sum((X - X_reconstructed) ** 2, axis=1)
```

Verify that the result has shape:

```python
(100,)
```

---

## Exercise 2 — Percentile Threshold

Calculate:

```python
threshold = np.percentile(scores, 95)
```

Count the flagged observations:

```python
np.sum(scores > threshold)
```

Compare the result to:

```python
5% of 100
```

Explain why the count may not always equal exactly 5.

---

## Exercise 3 — Compare Thresholds

Calculate thresholds using:

- 90th percentile
- 95th percentile
- 99th percentile

For each threshold calculate:

```python
number of flagged observations
```

Create a table:

```text
Threshold | Number Flagged
```

Observe the relationship.

---

## Exercise 4 — Normal vs Anomalous Data

Create `X_normal` with a strong linear relationship.

Then manually add 10 anomalies.

Fit PCA only on the normal data.

Calculate:

```python
normal_scores
anomaly_scores
```

Compare:

```python
np.mean(normal_scores)
np.mean(anomaly_scores)
```

---

## Exercise 5 — Different Component Counts

Run anomaly detection using:

- 1 component
- 2 components
- 3 components

Compare reconstruction errors.

Ask yourself:

Why might keeping too many components make reconstruction-based anomaly detection less useful?

---

## Challenge

Build:

```python
class PCAAnomalyDetector:
    ...
```

with:

- fit(X)
- score_samples(X)
- predict(X)

`fit(X)` should:

- fit PCA
- calculate training reconstruction scores
- determine a threshold

`score_samples(X)` should:

- transform
- reconstruct
- calculate row-level reconstruction error

`predict(X)` should return:

- 0 → normal
- 1 → anomaly

Example:

```python
detector = PCAAnomalyDetector(n_components=2, percentile=99)
detector.fit(X_train)
scores = detector.score_samples(X_test)
predictions = detector.predict(X_test)
```

---

## Bonus Challenge

Add:

```python
def decision_function(X):
    ...
```

Return:

```python
score - threshold
```

Then:

- negative → below threshold
- positive → above threshold

This is useful because it tells you not just whether an observation crossed the threshold, but how far it is from the threshold.
