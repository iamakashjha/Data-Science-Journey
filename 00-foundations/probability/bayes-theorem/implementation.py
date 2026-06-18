# Simple Bayes Example

P_A = 0.01      # Disease prevalence
P_B_given_A = 0.99
P_B = 0.02

posterior = (P_B_given_A * P_A) / P_B

print(posterior)