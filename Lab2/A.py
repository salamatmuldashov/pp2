a = list(map(int,input().split()))
j = 0
for i in range(len(a)):
    if j < i:
        break
    if j >= len(a)-1:
        print(1)
        exit()
    j = max(a[i]+i,j)
print(0)
    
    

    
     





    

 
    