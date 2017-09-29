"""
    Selection Sort
      Properties:
       Not stable
       O(1) extra space
       Θ(n2) comparisons
       Θ(n) swaps
       Not adaptive
"""
#to use comma seperated input uncomment below line
#x = [int(i) for i in input().strip().split(",")]

x=[10,9,8,7,6,5,4,3,2,1]
for i in range(len(x)-1):
    minn = i
    for j in range(i+1,len(x)):
        if(x[j] < x[minn]):
            minn=j
    if(minn!=i):
        x[i],x[minn] = x[minn],x[i]
print(x)
