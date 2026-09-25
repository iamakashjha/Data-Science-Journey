# Reflection - NumPy Aggregations & Statistics

## Understanding

### What is an aggregation?

An aggregation reduces many values into a smaller set of summary values. For example, taking the mean or total of an array is an aggregation.

### What does `np.mean()` calculate?

`np.mean()` calculates the arithmetic average of the values in an array or along a specified axis.

### What is the difference between mean and median?

The mean is the average value, while the median is the middle value after sorting. The median is often more robust when outliers are present.

### What does standard deviation tell us?

Standard deviation tells us how spread out a dataset is around its mean.

### What does `argmax()` return?

`argmax()` returns the index of the maximum value in the array or along a specified axis.

## Axis

### What does `axis=0` do?

It collapses rows and produces one result per column.

### What does `axis=1` do?

It collapses columns and produces one result per row.

### Why does `np.mean(X, axis=0)` return one value per feature?

Because it averages across all observations for each feature separately.

### Why does `np.sum(X, axis=1)` return one value per observation?

Because it sums across the columns of each row, creating one total per observation.

## Data Science

### Why would you calculate feature-wise mean and standard deviation before Machine Learning?

These values help you understand the center and spread of each feature, which is useful for feature engineering, preprocessing, and model interpretation.

### Why can a mean be misleading when a dataset contains outliers?

A few extreme values can pull the mean far away from the typical data point, making it seem more central than it really is.

### Why is `.shape` important when using `axis`?

The shape tells you whether the array is organized by rows = samples or columns = features, which determines the correct interpretation of each axis.

## Self assessment

- Basic statistics: ⭐⭐⭐⭐⭐
- Mean vs median: ⭐⭐⭐⭐⭐
- Standard deviation: ⭐⭐⭐⭐⭐
- `axis=0`: ⭐⭐⭐⭐⭐
- `axis=1`: ⭐⭐⭐⭐⭐
- `argmin` / `argmax`: ⭐⭐⭐⭐⭐
- Data science usage: ⭐⭐⭐⭐⭐
