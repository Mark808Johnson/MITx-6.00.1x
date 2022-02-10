# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print: Number of times bob occurs is: 2

count = 0
i = 0
s = "asdfuibbobobihuabbobasodifhgbob"

while i < len(s):
    if "bob" in s[i:i+3]:
        count += 1
    i += 1

print("Excepted number of time 'bob' occurs in string s: 4")
print("Actual Number of times 'bob' occurs in string s: " + str(count))
