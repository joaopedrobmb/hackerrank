# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

records = []
scores = []
names = []
    
for _ in range(int(input())):
    name = input()
    score = float(input())
    
    records += [[name, score]]
    scores += [score]

scores = sorted(list(set(scores)))
second_score = scores[1]

for sublist in records:
    if sublist[1] == second_score:
        names.append(sublist[0])

names = sorted(names)

for name in names:
    print(name)