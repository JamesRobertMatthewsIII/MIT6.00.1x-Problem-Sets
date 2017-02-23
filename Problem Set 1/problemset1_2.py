#! python3
"""
Problem 1.2
10.0 points possible (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2
"""

# test value. Do not include s in answer form
s = 'azcbobobegghakl'

bob_count = 0
lower_limit = 0
upper_limit = 3
while upper_limit <= len(s):
    if s[lower_limit:upper_limit] == 'bob':
        bob_count += 1
    lower_limit += 1
    upper_limit += 1

print("Number of times bob occurs is: %d" % (bob_count))
