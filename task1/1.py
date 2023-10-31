def sort_list_declorative(array):
    array.sort(reverse=True)
    return array
    
def sort_list_imperative(arr):
    num = arr
    for i in range(0,len(num)-1):
        for j in range(len(num)-1):
            if num[j]<num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num
    

numbers = [3,1,5,7,2]    
res2 = sort_list_declorative(numbers)
print(res2,"\n")
res = sort_list_imperative(numbers)
print(res,"\n")



