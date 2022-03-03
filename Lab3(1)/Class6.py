a = list(map(int,input().split()))
withprimes = list(filter(lambda i: all(i%j!=0 for j in range(2,i//2+1)),a))
print(withprimes)
