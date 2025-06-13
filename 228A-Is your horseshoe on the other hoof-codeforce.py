# Read input as a list of integers
s = list(map(int, input().split()))

# Use a set to count unique colors
unique_colors = len(set(s))

# Minimum horseshoes to buy = 4 - number of unique colors
print(4 - unique_colors)
