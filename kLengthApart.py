'''Given an array nums of 0s and 1s and an integer k, 
return True if all 1's are at least k places away from each other, otherwise return False.
'''
def kLengthApart(nums, k):
    i = 0
    prev = -1
    while i < len(nums):
        if nums[i] == 1:
            if prev != -1 and (i - (prev+1)) < k:
                return False
            prev = i    
        i+= 1
    return True

print(kLengthApart([1,0,0,1,0,1], 2))