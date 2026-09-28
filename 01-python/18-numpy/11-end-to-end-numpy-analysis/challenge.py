import numpy as np

# ----------------------------------------------------
# Customer intelligence report
# ----------------------------------------------------

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

# derived metrics
revenue_per_order = revenue / orders
return_rate = returns / orders
return_rate_percent = return_rate * 100

# statistics
print("==================================================")
print("CUSTOMER INTELLIGENCE REPORT")
print("==================================================")
print("Total Customers:", len(customers))
print("Total Revenue:", np.sum(revenue))
print("Average Revenue:", np.mean(revenue))
print("Median Revenue:", np.median(revenue))
print("Highest Revenue Customer:", customers[np.argmax(revenue)], revenue[np.argmax(revenue)])
print("Lowest Revenue Customer:", customers[np.argmin(revenue)], revenue[np.argmin(revenue)])

# top 3
revenue_order = np.argsort(revenue)[::-1]
print("\nTop 3 Customers:")
for idx in revenue_order[:3]:
    print(customers[idx], revenue[idx])

# top revenue per order
rpo_order = np.argsort(revenue_per_order)[::-1]
print("\nTop Customer by Revenue/Order:")
print(customers[rpo_order[0]], revenue_per_order[rpo_order[0]])

# highest return rate
print("\nHighest Return Rate:")
print(customers[np.argmax(return_rate)], return_rate[np.argmax(return_rate)])

# potential outliers
mean_revenue = np.mean(revenue)
std_revenue = np.std(revenue)
threshold = mean_revenue + 2 * std_revenue
outliers = revenue > threshold
print("\nPotential Revenue Outliers:")
print(customers[outliers])
print(revenue[outliers])

# high-value customers
high_value = revenue > 30000
print("\nHigh-Value Customers:")
print(customers[high_value])

# high-value + high-activity customers
engaged = (revenue > 30000) & (orders >= 15)
print("\nHigh-Value + High-Activity Customers:")
print(customers[engaged])
