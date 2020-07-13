def BinarySearch(arr, low, high, key):
    if(low==high):
        if(arr[low]==key):
            return low
        else:
            return 0
    else:
        mid=int((low+high)/2)
        if(arr[mid]==key):
            return mid
        if(key<arr[mid]):
            return BinarySearch(arr,low,mid-1,key)
        else:
            return BinarySearch(arr,mid+1,high,key)




index = BinarySearch([1,2,3,4,5,6,7,8],0,7,2)
print(index)


