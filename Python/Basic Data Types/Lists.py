# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

N = int(input())

result = []

for i in range(N):
    command, *vals = input().split()
    
    if command == 'append':
        result.append(int(vals[0]))
    elif command == 'insert':
        result.insert(int(vals[0]), int(vals[1]))
    elif command == 'print':
        print(result)
    elif command == 'remove':
        result.remove(int(vals[0]))
    elif command == 'sort':
        result.sort()
    elif command == 'pop':
        result.pop()
    elif command == 'reverse':
        result.reverse()
