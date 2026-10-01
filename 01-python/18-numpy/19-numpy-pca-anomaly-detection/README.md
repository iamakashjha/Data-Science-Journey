# Day 65 — PCA Anomaly Detection

## Objective

Use PCA reconstruction error as an anomaly signal.

## Topics

- anomaly detection
- PCA reconstruction
- reconstruction error
- anomaly scores
- threshold selection
- percentile thresholds
- false positives
- false negatives
- PCA limitations

## Core Idea

```text
Normal Data
    ↓
PCA
    ↓
Learn dominant structure
    ↓
Reconstruct
    ↓
Measure error
```

Observations with unusually large reconstruction errors may be flagged as anomalies.

## Core Formula

```python
scores = np.sum((X - X_reconstructed) ** 2, axis=1)
```

## Important Principle

Fit PCA on representative normal training data when using PCA reconstruction error for anomaly detection.

## Threshold

There is no universal threshold. Possible approaches include:

- percentile
- training score distribution
- domain knowledge
- validation data

## Applications

Conceptually useful for:

- sensor monitoring
- manufacturing
- system monitoring
- unusual transaction patterns
- quality control
- exploratory anomaly detection

## Limitations

PCA anomaly detection may struggle with:

- nonlinear relationships
- multiple clusters
- contaminated training data
- anomalies inside the PCA subspace
- poor feature scaling

---

## Day 65 Completion Checklist

- [ ] Created 19-numpy-pca-anomaly-detection
- [ ] Created all standard project files
- [ ] Understand what an anomaly is
- [ ] Understand PCA reconstruction error
- [ ] Calculated row-level anomaly scores
- [ ] Fit PCA on normal training data
- [ ] Used percentile thresholds
- [ ] Experimented with mean/std thresholds
- [ ] Understand threshold trade-offs
- [ ] Understand false positives
- [ ] Understand false negatives
- [ ] Compared component counts
- [ ] Understand PCA anomaly-detection limitations
- [ ] Completed all exercises
- [ ] Built PCAAnomalyDetector
- [ ] Answered 5 interview questions
- [ ] Completed reflection

## Where We Are Now

Your PCA progression now looks like:

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
├── 15-numpy-pca-foundations
├── 16-numpy-pca-reconstruction-whitening
├── 17-numpy-pca-from-scratch
├── 18-numpy-feature-selection-dimensionality-reduction
└── 19-numpy-pca-anomaly-detection   ← Day 65

## Day 65 Core Takeaway

PCA reconstruction error can act as an anomaly score: observations that are poorly represented by a learned low-dimensional structure receive larger errors. But the threshold, training data, component count, feature scaling, and data distribution all affect whether that signal is useful.
