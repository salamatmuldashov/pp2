x = int(input())
t = "@gmail.com"
for i in range(x):
     s = input()
     if t in s:
         s = s.replace(t,"")
         print(s)
    


