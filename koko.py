import math
def koko(arr,k):
    def total(arr,k):
        totalhours =0
        
        for i in range(len(arr)):
                totalhours = totalhours+ math.ceil(arr[i]/k)
        return totalhours
# total([3,6,7,11],8)
# def koko(arr,k):
    l = 1
    n = len(arr)
    h = max(arr)
    ans = -1
    while l<=h:
        mid = (l+h)//2
        totalhours = 0
        totalhours = total(arr,k)
        if totalhours <= k:
            ans = mid
            h= mid-1
        else:
            l= mid+1
        return print(ans)
koko([3,6,7,11],8)


