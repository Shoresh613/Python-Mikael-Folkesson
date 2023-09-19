import random

n = 1

results = [[], [], [], [], [], []]

results_dict = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
}

# Toss the dice 10^n times, store results in separate list for each run
while n <= 6:
    for k in range(10**n):
        results[n-1].append(random.randint(1, 6))
    n += 1

# Accumulate counts for each die face
for r in results:
    for j in range(1, 7):
        count = r.count(j)
        results_dict[j].append(count)

# Calculate frequencies for each die face
for j in range(1, 7):
    count_list = results_dict[j]
    total_count = sum(count_list)
    freq_list = [count / total_count for count in count_list]
    results_dict[j] = [total_count, freq_list]

print(results_dict)
