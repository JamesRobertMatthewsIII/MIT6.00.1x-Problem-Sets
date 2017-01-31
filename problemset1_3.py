#! python3
"""
Problem 1.3
15.0 points possible (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print
Longest substring in alphabetical order is: abc
"""

# test case. Do not include s in answer form
s = 'azcbobobegghakl'

s = s.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
current_longest = s[0]
lower_limit = 0
for character in s:
    upper_limit = lower_limit + 1
    while upper_limit < len(s):
        sub_string = s[lower_limit:upper_limit]
        if alphabet.find(s[upper_limit - 1]) > alphabet.find(s[upper_limit]):
            lower_limit += 1
            break
        else:
            upper_limit += 1
    if len(sub_string) > len(current_longest):
        current_longest = sub_string
print("Longest substring in alphabetical order is: " + current_longest)
