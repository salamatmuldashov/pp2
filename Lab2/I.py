n = int(input())
list = []
cnt = 0
for i in range(n):
    s = input().split()
    if s[0] == '1':
        list.append((s[1]))
    if s[0] == '2':
        cnt+=1
       
arr=[]
for i in range(cnt):
    print(list[i],end=" ")
        





