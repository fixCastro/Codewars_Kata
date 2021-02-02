"""You are given an odd-length array of integers, in which all of them are the same, 
except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3"""

from functools import reduce

def stray(arr):
    # XOR is amazing
    return reduce(lambda x,y: x ^ y, arr)

if __name__ == '__main__':
    print(stray([17, 17, 3, 17, 17, 17, 17]))