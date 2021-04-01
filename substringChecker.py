'''
Given a string and a pattern, find the starting indices of all occurrences 
of the pattern in the string. For example, given the string "abracadabra" 
and the pattern "abr", you should return [0, 7].
'''


# I chose to use a basic Rabin-Karp sliding window solution, should run in O(n+m) time
# args: s - the given string where we will look for substrings
#       substr - the given subtring that we will look for starting indices within string s
def findSubstring(s, substr):
    starting_indices = []
    i = 0
    j = len(substr)
    h = hash(substr)
    while j < len(s):
        if hash(s[i:j] == h):
            starting_indices.append(i)
        i += 1
        j += 1
    return starting_indices