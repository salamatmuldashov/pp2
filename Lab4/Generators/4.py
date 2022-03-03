a,b = map(int,input().split())
def Squares(a,b):
    for i in range(a,b+1):
        yield i**2

for i in Squares(a,b):
    print(i,end=" ")