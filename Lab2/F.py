n = int(input())
a = {}
cnt = 0
for i in range(n):
    x,y = map(str,input().split())
    a.setdefault(x,cnt)
    a[x]+=int(y)

mx = 0
for i in a.items():
    mx = max(mx,i[1])

names = []
for i in a.items():
    if mx == i[1]:
        names.append((i[0],"is lucky!"))
    else:
        names.append((i[0],"has to receive",mx-i[1],"tenge"))

names.sort()
for i in names:
    print(*i)







    






