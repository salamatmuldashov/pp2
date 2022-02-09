a,b = map(int,input().split())
n = int(input())
list=[]
for i in range(n):
    x,y = map(int,input().split())
    list.append(((((((x-a)**2) + ((y-b))**2))**0.5),x,y))


list.sort()
for i in list:
    print(i[1],i[2])


    

