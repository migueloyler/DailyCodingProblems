'''
Write a function, throw_dice(N, faces, total), 
that determines how many ways it is possible 
to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
'''
def throw_dice(N, faces, total):
    if total < 0:
        return 0
    if N == 0 and total == 0:
        return 1
    if N == 0:
        return 0
    cnt = 0
    for i in range(1, faces+1):
        cnt += throw_dice(N-1, faces, total-i)
    return cnt

print(throw_dice(3,6,7))