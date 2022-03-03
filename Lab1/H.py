s = input()
t = input()
cnt = 0
for i in range(0,len(s)):
    if s[i] == t:
        cnt+=1

if (cnt == 1):
    for i in range(0,len(s)):
        if s[i] == t:
            print(i)
            exit(0)

else: 
    for i in range(0,len(s)):
        if s[i] == t:
            print(i,end=" ")
            break


    for i in reversed(range(len(s))):
        if s[i] == t:
            print(i)
            break


        




    
    

