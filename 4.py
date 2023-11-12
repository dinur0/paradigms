from functools import reduce
import math

def mean(array):
    return int(reduce((lambda x,y: x+y),array)/len(array))    
    
def minus_mean(arr):
    new_list = list(map(lambda x: x - mean(arr),arr))
    return new_list
    
def pirson(arr1,arr2):
    x = minus_mean(arr1)
    y = minus_mean(arr2)
    x2 = list(map(lambda u: u**2,minus_mean(arr1)))
    y2 = list(map(lambda u: u**2,minus_mean(arr2)))
    temp = range(0,len(x))
    res1 = sum(list(map(lambda i: x[i]*y[i],temp)))
    res2 = list(map(lambda i: x2[i]*y2[i],temp))
    res2 = math.sqrt(sum(x2)*sum(y2))
    return res1/res2


first = [2,4,6,8]
second = [2,4,10,12]
print(pirson(first,second))