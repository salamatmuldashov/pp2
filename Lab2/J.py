n = int(input())
x,y,z = 0,0,0
a = []
cnt = 0
for i in range(n):
    s = input()
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            x+=1
        if ord(char) >= 97 and ord(char) <= 122:
            y+=1
        if ord(char) >=48 and ord(char) <= 57:
            z+=1
    
    if x!=0 and y!=0 and z!=0:
        a.append(s)

    x,y,z = 0,0,0

a.sort()

d = {}
for i in a:
    d.setdefault(i)


for i in d:
    cnt+=1
    

print(cnt)
for i in d:
    print(i)


            

