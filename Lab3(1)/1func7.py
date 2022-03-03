def has_33(nums):
    for i in range(len(a)-1):
        if a[i] == 3 and a[i+1] == 3:
            print(True)
            exit()
    print(False)
                    
a = list(map(int,input().split()))
has_33(a)
