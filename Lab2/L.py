s = input()
a = []
for i in s:
    if i == '(' or i == '[' or i == '{':
        a.append(i)
    else:
        if (len(a) == 0):
            print("No")
            exit()  
        else:
            if(a[-1] == '(' and i == ')') or (a[-1] == '[' and i == ']') or (a[-1] == '{' and i == '}'):
                a.pop()
            else:
                a.append(i)
    
if len(a) == 0:
    print("Yes")
else:
    print("No")






    

     
