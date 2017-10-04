"""
    MERGE SORT:
    
    Stable
    Θ(n·lg(n)) time
    Not adaptive
    Does not require random access to data
"""
# input must be comma seperated integers
x = [int(i) for i in input().split(",") ]

def merge(left,right):
    result = []
    while( len(left) !=0 and len(right) !=0 ):
        if( left[0] <= right[0] ):
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    while( len(left) !=0 ):
        result.append(left[0])
        left.pop(0)
    while( len(right) != 0) :
        result.append(right[0])
        right.pop(0)
    return result

def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    i = int(len(arr)/2)
    left = arr[:i]
    right = arr[i:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

print(merge_sort(x))
