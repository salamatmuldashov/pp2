n = int(input())
name = []
values = []
while(n!=0):
    a,b = map(str,input().split())
    name[a]+=b
    n-=1
print(a)
