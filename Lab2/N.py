a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)
b = []
for i in range(len(a)//2):
    b.append(a[0] + a[-1])
    a.pop(0)
    a.pop(-1)
    if(len(a) == 1):
        b.append(a[0])

for i in b:
    print(i,end=" ")

    
