# Write a program to add two list and find the minimum number from the resultant list.

n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
res=[]
for i in range(0,n):
    x=l[i]+m[i]
    res.append(x)
print(min(res))
