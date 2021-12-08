# Split Strings
# Complete the solution so that it splits the string into pairs of two characters.
# If the string is empty return an empty list.
# If the string contains an odd number of characters then it should replace the
# missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('a') # should return ['a_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']


def split(string):
    if string == '':
        return []
    elif len(string) == 1:
        return [string+'_']
    else:
        return [string[:2]] + split(string[2:])

print(split('hello'))