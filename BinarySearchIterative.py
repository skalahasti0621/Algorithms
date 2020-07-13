# Binary search uses divide and conquer strategy 

def BinarySearch(arr, n, key):
    low=int(1)
    high=int(n)
    while(low<=high):
        mid=int(low+high)/2
        if(key==mid):
            return int(mid)
        elif(key<mid):
            high=mid-1
        else:
            low=mid+1
    return -1

print(BinarySearch({1,2,3,4,5,6,7,8,9},9,12))




