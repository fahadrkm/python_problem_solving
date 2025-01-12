# Input the number of scores
n = int(input())

# Input the scores as space-separated values and convert them to a list of integers
scores = list(map(int, input().split()))

# Remove duplicates by converting to a set, then back to a sorted list in descending order
unique_scores = sorted(set(scores), reverse=True)

# The runner-up score is the second element in the sorted list
print(unique_scores)
print(unique_scores[1])

2 3 6 6 5