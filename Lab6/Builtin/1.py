a = list(map(int,input().split()))
total = 1
for i in range(len(a)):
    total *= a[i]

print(total)