# kadame algorithm

def kadame(arr):
    max_so_far = arr[0]
    max_end = arr[0]
    for i in arr[1:]:
        max_so_far= max(i,i+max_so_far)
        max_end = max(max_so_far,max_end)
    return print(max_end)

kadame([2,-1,-3,5,6,0,5])