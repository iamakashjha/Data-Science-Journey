# Day 63 — PCA From Scratch

## Objective

Build a reusable PCA implementation using NumPy.

## Topics

- PCA class design
- fit()
- transform()
- fit_transform()
- inverse_transform()
- explained variance
- whitening
- data leakage
- train/test transformation

## Main Concepts

PCA learns its parameters from training data.

Those parameters are then reused to transform validation and test data.

## Core Workflow

```text
Training Data
     ↓
fit()
     ↓
Learn PCA
     ↓
transform()
     ↓
Reduced Training Data

Test Data
     ↓
transform()
     ↓
Reduced Test Data
```

## Machine Learning Connection

PCA can be used as a preprocessing step:

```text
Features
   ↓
Scaling
   ↓
PCA
   ↓
Model
```

## Important Principle

Never fit PCA independently on test data.

---

## Day 63 Completion Checklist

- [ ] Created 17-numpy-pca-from-scratch
- [ ] Created all standard project files
- [ ] Built a PCA class
- [ ] Implemented fit()
- [ ] Implemented transform()
- [ ] Implemented fit_transform()
- [ ] Implemented inverse_transform()
- [ ] Implemented whitening
- [ ] Added input validation
- [ ] Stored PCA parameters
- [ ] Tested n_components
- [ ] Tested train/test transformation
- [ ] Understood data leakage
- [ ] Calculated reconstruction error
- [ ] Completed the PCA challenge
- [ ] Answered 5 interview questions
- [ ] Completed reflection

## Where We Are Now

The PCA progression now looks like:

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
└── 17-numpy-pca-from-scratch   ← Day 63

## Day 63 Core Takeaway

A Data Scientist should understand not only how an algorithm works mathematically, but also how to turn that mathematics into reliable, reusable code. PCA's fit → transform → inverse_transform pattern is a practical example of that transition.
