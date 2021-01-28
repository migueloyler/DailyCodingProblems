'''
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.
'''
'''
def concatenatedBinary(n):
        bin_arr = []
        for i in range(1,n+1):
            bin_arr.append(bin(i)[2:])
        bin_string = ''.join(bin_arr)
        return int(bin_string, 2)

print(concatenatedBinary(2))
'''

def concatenatedBinary(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    my_num = 0
    to_shift = 0
    for i in range(1,n+1):
        my_num = (my_num << len(bin(i))-2) % (10**9 + 7)
        my_num = (my_num | i) % (10**9 + 7)
    return my_num 

#def concatenatedBinary(n):
#    return int(''.join([bin(i)[2:] for i in range(1,n+1)]),2) % (10**9 + 7)

print(concatenatedBinary(12))