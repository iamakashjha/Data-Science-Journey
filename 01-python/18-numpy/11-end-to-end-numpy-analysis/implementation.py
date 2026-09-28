import numpy as np


# ============================================================
# 1. DATA
# ============================================================

customers = np.array([
    "C001", "C002", "C003", "C004", "C005",
    "C006", "C007", "C008", "C009", "C010"
])

orders = np.array([
    12, 5, 20, 8, 15,
    3, 18, 10, 6, 25
])

revenue = np.array([
    24000, 7500, 42000, 12000, 30000,
    4000, 36000, 18000, 9000, 50000
])

returns = np.array([
    1, 0, 2, 1, 3,
    0, 4, 1, 0, 2
])


# ============================================================
# 2. VALIDATION
# ============================================================

assert len(customers) == len(orders)
assert len(customers) == len(revenue)
assert len(customers) == len(returns)

print("Data validation passed.")


# ============================================================
# 3. DERIVED METRICS
# ============================================================

revenue_per_order = revenue / orders
return_rate = returns / orders
return_rate_percent = return_rate * 100


# ============================================================
# 4. BASIC STATISTICS
# ============================================================

print("\n--- Revenue Statistics ---")
print("Total:", np.sum(revenue))
print("Mean:", np.mean(revenue))
print("Median:", np.median(revenue))
print("Minimum:", np.min(revenue))
print("Maximum:", np.max(revenue))
print("Standard deviation:", np.std(revenue))


# ============================================================
# 5. HIGH-VALUE CUSTOMERS
# ============================================================

high_value = revenue > 30000

print("\n--- High-Value Customers ---")
print(customers[high_value])
print(revenue[high_value])


# ============================================================
# 6. HIGH-VALUE + HIGH-ACTIVITY
# ============================================================

engaged = (
    (revenue > 30000) &
    (orders >= 15)
)

print("\n--- High-Value + High-Activity ---")
print(customers[engaged])


# ============================================================
# 7. HIGH RETURN RATE
# ============================================================

high_return_rate = return_rate > 0.15

print("\n--- High Return Rate ---")
print(customers[high_return_rate])
print(return_rate_percent[high_return_rate])


# ============================================================
# 8. REVENUE RANKING
# ============================================================

revenue_ranking = np.argsort(revenue)[::-1]

print("\n--- Revenue Ranking ---")
for index in revenue_ranking:
    print(customers[index], revenue[index])


# ============================================================
# 9. TOP 3
# ============================================================

top_3_indices = revenue_ranking[:3]

print("\n--- Top 3 Customers ---")
for index in top_3_indices:
    print(customers[index], revenue[index])


# ============================================================
# 10. BOTTOM 3
# ============================================================

ascending = np.argsort(revenue)
bottom_3_indices = ascending[:3]

print("\n--- Bottom 3 Customers ---")
for index in bottom_3_indices:
    print(customers[index], revenue[index])


# ============================================================
# 11. MAXIMUM / MINIMUM
# ============================================================

max_index = np.argmax(revenue)
min_index = np.argmin(revenue)

print("\n--- Extreme Values ---")
print("Highest:", customers[max_index], revenue[max_index])
print("Lowest:", customers[min_index], revenue[min_index])


# ============================================================
# 12. REVENUE PER ORDER RANKING
# ============================================================

rpo_ranking = np.argsort(revenue_per_order)[::-1]

print("\n--- Revenue Per Order Ranking ---")
for index in rpo_ranking:
    print(customers[index], revenue_per_order[index])


# ============================================================
# 13. OUTLIER DETECTION
# ============================================================

mean_revenue = np.mean(revenue)
std_revenue = np.std(revenue)
threshold = mean_revenue + 2 * std_revenue

outliers = revenue > threshold

print("\n--- Potential Outliers ---")
print(customers[outliers])
print(revenue[outliers])


# ============================================================
# 14. NORMALIZATION
# ============================================================

revenue_norm = (
    revenue - np.min(revenue)
) / (
    np.max(revenue) - np.min(revenue)
)

orders_norm = (
    orders - np.min(orders)
) / (
    np.max(orders) - np.min(orders)
)

return_norm = (
    return_rate - np.min(return_rate)
) / (
    np.max(return_rate) - np.min(return_rate)
)


# ============================================================
# 15. CUSTOMER SCORE
# ============================================================

customer_score = (
    0.5 * revenue_norm +
    0.3 * orders_norm -
    0.2 * return_norm
)


# ============================================================
# 16. SCORE RANKING
# ============================================================

score_ranking = np.argsort(customer_score)[::-1]

print("\n--- Customer Score Ranking ---")
for index in score_ranking:
    print(customers[index], customer_score[index])
