# Write a program to print minimum value from the two list.

l=list(map(int,input().split()))
m=list(map(int,input().split()))
l.extend(m)
print(min(l))

