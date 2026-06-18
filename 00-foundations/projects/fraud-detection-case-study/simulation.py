fraud_rate = 0.01

transactions = 10000

fraud_transactions = int(
    transactions * fraud_rate
)

print("Fraud Transactions:",
      fraud_transactions)


# How many fraud cases would we expect in 10,000 transactions?