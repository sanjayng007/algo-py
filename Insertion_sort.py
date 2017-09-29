"""
  Insertion Sort
    Stable
    O(1) extra space
    O(n2) comparisons and swaps
    Adaptive: O(n) time when nearly sorted
    Very low overhead
"""
#Use comma seperated input

x = [int(i) for i in input().strip().split(",")]

i = 1

while( i < len(x) ):
    j = i
    while( j>0 and x[j-1] > x[j]):
        x[j] , x[j-1] = x[j-1] , x[j]
        j-=1
    i+=1

print(x)
