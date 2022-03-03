def Reverser(s):
    a = list(s)
    a.reverse()
    for i in a:
        print(i,end=" ")
        



s = input().split()
Reverser(s)