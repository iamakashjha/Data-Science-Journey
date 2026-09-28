import numpy as np

# ----------------------------------------------------
# Customer dataset
# ----------------------------------------------------

customer_ids = np.array([
    "C001",
    "C002",
    "C003",
    "C004",
    "C005",
    "C006",
    "C007",
    "C008"
])

revenue = np.array([
    1200,
    5400,
    800,
    3200,
    7600,
    2100,
    4500,
    1800
])

orders = np.array([
    5,
    21,
    3,
    14,
    31,
    8,
    19,
    7
])

print("Customer IDs:")
print(customer_ids)
print("\nRevenue:")
print(revenue)
print("\nOrders:")
print(orders)

# Part A - highest revenue customer
max_revenue_index = np.argmax(revenue)
print("\nPart A - Highest revenue customer:")
print(customer_ids[max_revenue_index], revenue[max_revenue_index])

# Part B - lowest revenue customer
min_revenue_index = np.argmin(revenue)
print("\nPart B - Lowest revenue customer:")
print(customer_ids[min_revenue_index], revenue[min_revenue_index])

# Part C - rank all customers by revenue
revenue_order = np.argsort(revenue)
print("\nPart C - Ranked by revenue ascending:")
for idx in revenue_order:
    print(customer_ids[idx], revenue[idx])

# Part D - top 3 customers
print("\nPart D - Top 3 customers:")
for idx in revenue_order[::-1][:3]:
    print(customer_ids[idx], revenue[idx])

# Part E - bottom 3 customers
print("\nPart E - Bottom 3 customers:")
for idx in revenue_order[:3]:
    print(customer_ids[idx], revenue[idx])

# Part F - customer with the most orders
max_orders_index = np.argmax(orders)
print("\nPart F - Customer with the most orders:")
print(customer_ids[max_orders_index], orders[max_orders_index])

# Part G - revenue per order
revenue_per_order = revenue / orders
print("\nPart G - Revenue per order:")
for i in range(len(customer_ids)):
    print(customer_ids[i], revenue_per_order[i])

# Part H - rank customers by revenue per order
rpo_order = np.argsort(revenue_per_order)[::-1]
print("\nPart H - Ranked by revenue per order:")
for idx in rpo_order:
    print(customer_ids[idx], revenue_per_order[idx])

# ----------------------------------------------------
# Advanced challenge
# ----------------------------------------------------

high_value_mask = (revenue > 3000) & (orders > 10)
high_value_customers = customer_ids[high_value_mask]
high_value_revenue = revenue[high_value_mask]

print("\nAdvanced challenge - High-value customers:")
print(high_value_customers)
print(high_value_revenue)

high_value_order = np.argsort(high_value_revenue)[::-1]
print("\nAdvanced challenge - Ranked by revenue:")
for idx in high_value_order:
    print(high_value_customers[idx], high_value_revenue[idx])

