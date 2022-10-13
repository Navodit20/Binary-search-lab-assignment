# Name: Navodit Gupta
# SID: 21107082
# Branch: Mechanical
'''
We can search an element in an array whose size is unknown in O(logn) time complexity provided that the array is in sorted order.
We can do this by making some modification in binary search technique.
The concept behind this approach is:
  ->Take inital value of i as 0 and j as 1.
  ->Now increase j to j*2 until arr[j] exceed the key to be searched.
  ->Now search the key using binary search between i and j.
'''
def binary_search(arr,l,r,x):
 
    if r >= l:
        mid = l+(r-l)//2
 
        if arr[mid] == x:
            return mid
 
        if arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
 
        return binary_search(arr,mid+1,r,x)
 
    return -1
 
# function takes an infinite size array and a key to be
# searched and returns its position if found else -1.
# We don't know size of a[] and we can assume size to be
# infinite in this function.

def findPos(a, key):
 
    l, h, val = 0, 1, arr[0]
 
    # Find h to do binary search
    while val < key:
        l = h            #store previous high
        h = 2*h          #double high index
        val = arr[h]       #update new val
 
    # low and high are updated
    # use binary search between them
    return binary_search(a, l, h, key)
 
# Driver function
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170] #change array
element = 100 #change which element you wish to find
ans = findPos(arr,element)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans)
