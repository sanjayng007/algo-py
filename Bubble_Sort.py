#Bubble Sort
"""
  Properties:
    Stable
    O(1) extra space
    O(n2) comparisons and swaps
    Adaptive: O(n) when nearly sorted
"""

x = [int(i) for i in input().strip().split(",")]

for i in range(1,len(x)):
    sorted = True
    for j in range(0,len(x)-i):
        if(x[j] > x[j+1]):
            x[j],x[j+1] = x[j+1],x[j]
            sorted = False
    if(sorted):
        break

print(x)
