import random

heads_heads = 0
trials = 10000

for _ in range(trials):
    toss1 = random.choice(["H", "T"])
    toss2 = random.choice(["H", "T"])

    if toss1 == "H" and toss2 == "H":
        heads_heads += 1

print(heads_heads / trials)