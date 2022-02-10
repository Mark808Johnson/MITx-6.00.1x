# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print-
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print-
# Longest substring in alphabetical order is: abc

s = 'ccnecwxfuulnhbqmdbqzbgo'
alp = "abcdefghijklmnopqrstuvwxyz"
max_string = ""
current_string = ""
letter_loc_prev = 0

for letter in s:
    if letter in alp:
        letter_loc_now = alp.find(letter)
        if letter_loc_now >= letter_loc_prev:
            current_string += letter
        else:
            if len(current_string) > len(max_string):
                max_string = current_string
                current_string = letter
            else:
                current_string = letter
        letter_loc_prev = letter_loc_now
if len(current_string) > len(max_string):
    max_string = current_string

print("Expected longest substring in alphabetical order of string 's' is: ccn")
print("Longest substring in alphabetical order of string 's' is: ", max_string)