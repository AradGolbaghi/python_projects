# [1,12,43,5,23]
# [1,12,43,5213,23]
#[1000,2]
#[1]
 

def big(big):
    max = 0
    for x in range(len(big)):
        if(big[x] > max):
            max = big[x]
            print( max)
            print("---------------")
            
    return max
    
print(big([1,12,43,5213,23]))