# Write a Python function, odd, that takes in one number and returns
# True when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x % 2 != 0

x = 4
print(f"{x} is an odd number- {odd(x)}")
