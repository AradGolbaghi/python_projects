# [1,12,43,5,23]
# [1,12,43,5213,23]
#[1000,2]
#[1]
 

import sys


def small(s_mall):
    min = 10000000000000000000000000000000000000000000000
    for x in range(len(s_mall)):
        if(s_mall[x] < min):
            min = s_mall[x]
            
    return min
    
print(small([0,-100,1,12,43,5213,23]))