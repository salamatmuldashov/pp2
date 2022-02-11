t = {}
n = int(input())
for i in range(n):
    x,y = map(str, input().split())
    t.setdefault(y,0)
    t[y] += 1
    

m = int(input())
for i in range(m):
    q,w,e = input().split()
    e = int(e)
    if w in t:
        t[w]-=e
        
ttl = 0
for i in t.values():
    if i > 0:
        ttl+=i

print("Demons left: " + str(ttl) )



    



