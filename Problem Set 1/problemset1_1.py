#! python3
"""
Problem 1.1
10.0 points possible (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

# test value. Do not include in answer
s = 'azcbobobegghakl'

vowels = 'aeiou'
s = s.lower()
vowel_count = 0
for character in s:
    if character in vowels:
        vowel_count += 1
print(vowel_count)
