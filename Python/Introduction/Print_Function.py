# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.

# Example

# Print the string .

# Input Format

# The first line contains an integer .

# Output Format

# Print the list of integers from 1 through n as a string, without spaces.

n = int(input())

numbers = list(range(0,n))
result = ''

for number in numbers:
    result += f'{number+1}'
    
print(result)