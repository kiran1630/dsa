def search(a,k):
    
    r = len(a)
    c = len(a[0])
    for i in range(r):
        print(a[i][0],a[i][-1])
        if a[i][0] <= k and a[i][-1] >= k:
            l= 0
            h = r*c-1
            while l<=h:
                mid = (l+h) //2
                row,col = divmod(mid,r)
                if a[row][col] == k:
                    print(a[row][col])
                    return True
                elif a[row][col]<k:
                    l= mid+1
                else:
                    h =mid-1
    else:
            print('not')
            return False

search([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)
