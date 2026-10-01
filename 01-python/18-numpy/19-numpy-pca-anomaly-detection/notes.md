# Day 65 Notes

## PCA Anomaly Detection

PCA can identify observations that are poorly represented by the dominant structure of the data.

## Core Formula

```python
residuals = X - X_reconstructed
scores = np.sum(residuals ** 2, axis=1)
```

## Workflow

```text
Normal Data
    ↓
Fit PCA
    ↓
Reconstruct
    ↓
Training Scores
    ↓
Threshold
    ↓
New Data
    ↓
Score
    ↓
Flag
```

## Threshold

```python
threshold = np.percentile(train_scores, 99)
```

## Important

A high score means: "poorly represented by the PCA subspace."

It does not automatically prove that an observation is an anomaly.

## Training Data

For anomaly detection, PCA should generally be fitted on representative normal data.

## Why?

Anomalies can otherwise influence the learned PCA subspace.

## Threshold Trade-Off

- Lower threshold: more detections, potentially more false positives
- Higher threshold: fewer detections, potentially more false negatives

## Component Selection

- Too few components: normal variation may be reconstructed poorly
- Too many components: unusual observations may also be reconstructed too well

## Limitations

PCA assumes a useful low-dimensional structure. It may perform poorly for nonlinear or highly multimodal data.
