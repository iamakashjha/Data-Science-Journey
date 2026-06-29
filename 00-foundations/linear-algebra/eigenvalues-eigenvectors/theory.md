# Day 27 — Eigenvalues & Eigenvectors (Intuition First)
**Goal:**

Your goal is to understand why eigenvalues and eigenvectors exist and why Data Scientists care about them.

By the end of today, you should understand:

- What an eigenvector is
- What an eigenvalue is
- Why they matter in Data Science
- How they connect to Principal Component Analysis (PCA)

## Step 1 — Imagine Stretching a Rubber Sheet

Imagine drawing several arrows on a rubber sheet.

Now stretch the sheet.

Most arrows:

- change direction
- change length

But a few special arrows:

- keep the same direction
- only become longer or shorter

Those special arrows are **eigenvectors**.

The amount they stretch is the **eigenvalue**.

## Step 2 — Mathematical Definition

If a matrix transforms a vector without changing its direction:

Where:
```
A = transformation matrix
v = eigenvector
λ (lambda) = eigenvalue
```
Interpretation:

The matrix transforms the vector by **scaling** it, not rotating it.

## Step 3 — Visual Intuition

Imagine a square.

A transformation stretches it.

Most arrows rotate.

One arrow still points in exactly the same direction.

That arrow is the eigenvector.


## Step 5 — Why Data Scientists Care

Imagine a dataset:
```
Height	Weight
170 	65
175	    70
180	    75
185	    80
```
These features are related.

Instead of keeping both dimensions, PCA finds:

- the direction with the most information
- the direction with the least information

Those directions come from **eigenvectors**.

