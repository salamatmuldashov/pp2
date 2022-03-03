n = int(input())
def Generator(n):
    for i in range(n,0,-1):
        yield i

mygenerator = Generator(n)
for i in mygenerator:
    print(i,end=" ")