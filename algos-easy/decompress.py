# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.
def decompress(s):
    result = []

    i = 0; j = 0
    
    numbers = '0123456789'


    while j < len(s):
        if s[j] in numbers: 
            j += 1
        else:
            #extract number from string using the difference b/w i&j
            num = int(s[i:j])
            result.append(num * s[j])
            # multiply the number by the char
            j += 1
            i = j 

    return ''.join(result)        



# TEST CASES
decompress("2c3a1t") # -> 'ccaaat'
# decompress("4s2b") # -> 'ssssbb'
# decompress("2p1o5p") # -> 'ppoppppp'
# decompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
# decompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
