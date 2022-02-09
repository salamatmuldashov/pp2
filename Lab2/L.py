s = input()
a = []
for i in s:
    if i == '(' or i == '[' or i == '{':
        a.append(i)
    if (i == ')' and a[-1] == '(') or (i == ']' and a[-1] == '[') or (i == '}' and a[-1] == '{'):
        a.pop()

if a:
    print("No")
else:
    print("Yes")

    

     
