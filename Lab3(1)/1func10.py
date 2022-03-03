def Unique(a):
    new = set(a)
    for i in new:
        print(i,end=" ")


a = list(map(int,input().split()))
Unique(a)