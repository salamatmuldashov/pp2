from string import ascii_lowercase, ascii_uppercase

n = int(input())
numbers = "1234567890"
list = []
for i in range(n):
    s = input()
    x,y,z = 0,0,0
    for j in s:
        if j in numbers:
            x += 1
        if j in ascii_uppercase:
            y += 1
        if j in ascii_lowercase:
            z += 1
    if x > 0 and y > 0 and z > 0:
        list.append(s)
        

list.sort()
print(len(list))
for i in list:
    print(i)