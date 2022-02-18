def Histogram(a):
    for i in range(len(a)):
        for j in range(a[i]):
            print("*",end="")
        print()
        


a = list(map(int,input().split()))
Histogram(a)
