n = int(input()) 
 
def Generator(n):
    for i in range(n):
        if i**2 <= n:
            yield i**2


mygenerator = Generator(n)
for i in mygenerator:
    print(i)


