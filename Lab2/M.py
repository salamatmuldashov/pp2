a = []
while True:
    s = input().split()
    if s[0] == '0':
        break
    a.append((s[2],s[1],s[0]))

a.sort()
b=[]
for i in a:
    b.append((i[2],i[1],i[0]))
    

for i in b:
    print(*i)
    

