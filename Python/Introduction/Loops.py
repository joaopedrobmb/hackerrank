# Task
# The provided code stub reads an integer, n , from STDIN. For all non-negative integers , print i^2 .

# Example

# The list of non-negative integers that are less than n=3 is [0,1,2] . Print the square of each number on a separate line.

# 0
# 1
# 4
# Input Format

# The first and only line contains the integer, .

# Output Format
# Print  lines, one corresponding to each .

n = int(input())

for i in range(0, n, 1):
    print(i**2)