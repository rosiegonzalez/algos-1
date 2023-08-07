# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


print(anagrams('restful', 'fluster'))

# Dhru's method
# list -> looking things up require you to iterate thru the whole list
# Dict/Object -> looking things up require a key (instant)
def anagrams(s1, s2):
    # first, check for strings length
    # check each letter in s1 with a letter in s2
    # Initialize a dict to hold the letters present in first string
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    for char in s2:
        if char not in count:
            return False
        else:
            count[char] -+ 1
            if count[char] < 0:
                return False

        print('count dict after second loop: ', count)
    return True




anagrams('restful', 'fluster')  # -> True
# anagrams('cats', 'tocs') # -> False
# anagrams('monkeyswrite', 'newyorktimes') # -> True
# anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# anagrams('pp', 'oo') # -> False
