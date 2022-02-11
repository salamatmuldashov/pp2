s = input()
s = s.replace(",","")
s = s.replace("!","")
s = s.replace("?","")
s = s.replace(".","")
s = s.replace(":","")

s = s.split()
cnt = 0
a = []
for i in s:
    a.append(i)
a.sort()
b = {}
for i in a:
    b.setdefault(i)



print(len(b))
for i in b:
    print(i)


    
    





