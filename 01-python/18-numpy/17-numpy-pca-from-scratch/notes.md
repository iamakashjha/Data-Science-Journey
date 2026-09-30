# Day 63 Notes

## Main Idea

Turn the PCA mathematics from previous days into a reusable Python class.

## PCA API

```python
pca = PCA(n_components=3)
```

## Fit

```python
pca.fit(X)
```

Learns PCA parameters.

## Transform

```python
pca.transform(X)
```

Applies learned parameters.

## Fit Transform

```python
pca.fit_transform(X)
```

Fits and transforms.

## Inverse Transform

```python
pca.inverse_transform(X_reduced)
```

Reconstructs the data.

## Important Attributes

```python
pca.mean_
pca.components_
pca.eigenvalues_
pca.explained_variance_
pca.explained_variance_ratio_
```

## Important Rule

Never fit PCA separately on test data.

Fit on training data:

```python
pca.fit(X_train)
```

Then transform:

```python
pca.transform(X_train)
pca.transform(X_test)
```

## Why?

To prevent data leakage.

## Component Shapes

If:

```python
X = (n_samples, n_features)
```

and:

```python
n_components = k
```

then:

```python
components_ = (k, n_features)
transformed X = (n_samples, k)
```

## Whitening

Whitening scales principal component scores so their variance is approximately one.
