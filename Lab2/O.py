s = str(input().split())
a = ["ZER","ONE","TWO","THR","FOU","FIV","SIX","SEV","EIG","NIN"]
index = s.find("+")
b=[]
c=[]

for i in range(2,index-2,3):
    b.append(s[i:i+3])

print()

for i in range(index+1,len(s)-3,3):
    c.append(s[i:i+3])

for i in a:
    if i in b:
        print(i)
