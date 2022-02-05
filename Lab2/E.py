from operator import xor


n, m = map(int,input().split())
a = []
for i in range(0,n):
    a[i] = m + (2*i)

sum = 0
for i in range(0,n):
    sum^=a[i]

print(sum)
