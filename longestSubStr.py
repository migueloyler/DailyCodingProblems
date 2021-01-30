'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    
    #disgusting O(n^2) approach
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if len(s) == 0:
            return 0
        max_len = 1
        for i in range(n):
            for j in range(i,n+1):
                if len(set(s[i:j])) == len(s[i:j]):
                    if len(s[i:j]) > max_len:
                        max_len = len(s[i:j])
        return max_len
    '''
    
    #beautiful O(n) apprach I figured out after some more thought
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == len(set(s)):
            return len(s)
        n = len(s)
        start_index = 0
        stop_index = 1
        max_len = 0
        while stop_index <= n:
            substr = s[start_index:stop_index]
            if len(substr) == len(set(substr)):
                if len(substr) > max_len:
                    max_len = len(substr)
                stop_index+=1
                continue
            while len(set(substr)) < len(substr):
                start_index += 1
                substr = s[start_index:stop_index]
                
        return max_len
