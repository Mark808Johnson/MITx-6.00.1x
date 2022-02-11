# Consider the following sequence of expressions:
#
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.
#
# This time, write a procedure, called biggest, which returns the key corresponding to the entry
# with the largest number of values associated with it. If there is more than one such entry,
# return any one of the matching keys.
#
# Example usage:
#
# >>> biggest(animals)
# 'd'

# If there are no values in the dictionary, biggest should return None.

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest_value = len(max(aDict.values()))
    for key in aDict:
        if len(aDict[key]) == biggest_value:
            return key

dictionary_a = {'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}
print("Dictionary: ", dictionary_a)
print(f"Expected key with largest number of values in Dictionary: b")
print(f"Calculated key with largest number of values in Dictionary: {biggest(dictionary_a)}")


