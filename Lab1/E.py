x,y = map(int,input().split())
flag = True
if x > 1:
    for i in range(2,x):
        if x % i == 0:
            flag = False

if x < 500:
    if flag == True:
        if y % 2 == 0:
            print("Good job!")
            exit(0)


print("Try next time!")







