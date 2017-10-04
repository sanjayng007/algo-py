"""
    QUICK SORT
    
    O(n2) time, but typically O(n·lg(n)) time
    Not adaptive
"""
arr=[int(i) for i in input().split(",")]

#Partition function

def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):

        if( arr[j] <= pivot ):

            i+=1
            arr[i] , arr[j] = arr[j] , arr[i]

    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return i+1

#main quicksort function

def quicksort (arr,low,high):
    if( low < high ):
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

quicksort(arr,0,len(arr)-1)
print(arr)
