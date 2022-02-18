def check_prime(x):
    for i in range(2,(x//2)+1):
        if x % i == 0:
            return False

    return True

    
def filter_prime(a):
    new = []
    for i in range(2,len(a)):
        if check_prime(i):
            new.append(i)

    print(new)


a = list(map(int,input().split()))
filter_prime(a)

