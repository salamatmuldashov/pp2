def order(a):
    new = []
    for i in range(len(a)):
        if a[i] == 0:
            new.append(a[i])
        if a[i] == 7:
            new.append(a[i])

    
    if new[0] == 0 and new[1] == 0 and new[2] == 7:
        print(True)
        exit()
    else:
        print(False)
        exit()
    
        

a = list(map(int,input().split()))
order(a)