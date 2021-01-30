'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
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