# Task
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format

# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .

# Output Format

# Print the result of .

n = int(input())
integer_list = map(int, input().split())

t = tuple(integer_list)

print(hash(t))