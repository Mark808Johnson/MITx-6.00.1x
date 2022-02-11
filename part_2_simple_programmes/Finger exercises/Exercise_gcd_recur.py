# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder. For example,
#
# gcd(2, 12) = 2
#
# gcd(6, 12) = 6
#
# gcd(9, 12) = 3
#
# gcd(17, 12) = 1
#
# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors.
# Suppose that a and b are two positive integers:
#
# If b = 0, then the answer is a
#
# Otherwise, gcd(a, b) is the same as gcd(b, a % b)

# Write a function gcdRecur(a, b) that implements this idea recursively.
# This function takes in two positive integers and returns one integer.

# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Your code here
#     remainder = max(a, b) % min(a, b)
#     if remainder != 0:
#         return gcdRecur(min(a, b), remainder)
#     else:
#         return min(a, b)

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

x = 10
y = 12
print(f"Expected greatest common divisor of {x} and {y} is 2")
print(f"Given greatest common divisor of {x} and {y} is {gcdRecur(x, y)}")
