# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5

s = "asdofijnpoaiouebrtsdf"
vowels = "aeiou"
vowel_count = 0

for word in s:
    for vowel in vowels:
        if word == vowel:
            vowel_count += 1

print("Excepted number of vowels: 9")
print("Actual number of vowels: " + str(vowel_count))
