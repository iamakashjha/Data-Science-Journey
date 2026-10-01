# Day 65 — PCA Anomaly Detection

## Main Idea

PCA can be used to identify observations that are poorly represented by a low-dimensional principal-component subspace.

## Workflow

```text
Normal Training Data
        ↓
       PCA
        ↓
Learn Normal Structure
        ↓
Reconstruct Training Data
        ↓
Calculate Reconstruction Scores
        ↓
Choose Threshold
        ↓
New Data
        ↓
Transform
        ↓
Reconstruct
        ↓
Calculate Score
        ↓
Compare With Threshold
```

## Reconstruction Score

For each observation:

```python
residual = X - X_reconstructed
score = np.sum(residual ** 2, axis=1)
```

### Interpretation

- low score: well represented by PCA
- high score: poorly represented by PCA

A high score is an anomaly signal, not absolute proof that the observation is anomalous.

## Threshold Methods

Possible approaches:

- percentile
- training score distribution
- domain-specific threshold
- validation-based threshold

## Important Principle

Fit PCA on representative normal training data when using reconstruction error to detect anomalies.

## Threshold Trade-Off

Lower threshold:

- more flagged observations
- potentially more false positives

Higher threshold:

- fewer flagged observations
- potentially more false negatives

## Limitations

PCA anomaly detection may struggle with:

- nonlinear structure
- multiple clusters
- contaminated training data
- anomalies aligned with the PCA subspace
- poorly scaled features
- complex distributions
