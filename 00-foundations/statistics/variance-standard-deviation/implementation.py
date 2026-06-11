def mean(values):
    return sum(values) / len(values)

def variance(values):
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)

def std_dev(values):
    return variance(values) ** 0.5

numbers = [2, 4, 6]

print("Mean:", mean(numbers))
print("Variance:", variance(numbers))
print("Std Dev:", std_dev(numbers))