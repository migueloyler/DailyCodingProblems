'''
Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.solutions = [None for i in range(len(nums))]


    def solve(self, subseq, i):

        if i == len(self.nums) - 1:
            self.solutions[i] = len(subseq)
            return len(subseq)

        if self.solutions[i] != None:
            print(subseq)
            return self.solutions[i]
        if self.nums[i] > subseq[-1]:
            w = self.solve([*subseq,self.nums[i]], i + 1)
        else:
            w = self.solve([-1,self.nums[i]], i + 1)
            
        w_o = self.solve(subseq, i+1)
        return max(w, w_o)


solutionObj = Solution([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
print(solutionObj.solve([-1],0))