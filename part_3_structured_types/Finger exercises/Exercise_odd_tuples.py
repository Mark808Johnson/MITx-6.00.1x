# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
# where every other element of the input tuple is copied, starting with the first one.
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input
# would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return aTup[0: len(aTup): 2]

tup = (1, 3, 4, 5, 6, 7, 8)
print(f"Function return new tuple which contains every other element of tuple {tup}")
print(f"Result: {oddTuples(tup)}")
