a = list(input().split())
if len(a) == 1:
    w = int(input())
    a.append(w)

x = int(a[0])
y = int(a[1])
arr = []
for i in range(x):
    arr.append(y+(2*i))

sum = 0
for item in  arr:
    sum = sum ^ item

print(sum)
    




# sum = 0
# for i in range (len(s)):
#     sum = sum ^ s[i]

# print(sum)




   
    


