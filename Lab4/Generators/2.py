n = int(input())
def Generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
    
mygenerator = Generator(n)
for i in mygenerator:
    print(i,end=", ")
