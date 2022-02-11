def rec(r):
    if(r=='ONE'): return(1)
    elif(r=='TWO'): return(2)
    elif(r=='THR'): return(3)
    elif(r=='FOU'): return(4)
    elif(r=='FIV'): return(5)
    elif(r=='SIX'): return(6)
    elif(r=='SEV'): return(7)
    elif(r=='EIG'): return(8)
    elif(r=='NIN'): return(9)
    elif(r=='ZER'): return(0)
def rc(o):
    if(o=='1'): return('ONE')
    elif(o=='2'): return('TWO')
    elif(o=='3'): return('THR')
    elif(o=='4'): return('FOU')
    elif(o=='5'): return('FIV')
    elif(o=='6'): return('SIX')
    elif(o=='7'): return('SEV')
    elif(o=='8'): return('EIG')
    elif(o=='9'): return('NIN')
    elif(o=='0'): return('ZER')


a = input()
mx=0
b = ''
t = 0

u = int(0)
sum1=int(0)
sum2=int(0)
for i in a:
    if(i != '+'):
        t+=1
    if(t<=3):
        b+=i
    else:
        sum2=sum1
        sum1=0
        u=0 
        t=0 
    if(t==3):
        y=rec(b)
        sum1=sum1*(10**u)+y
        t=0
        b=''
        u=1
ans=sum1+sum2
answer=''
word=str(ans)
for i in word:
    answer+=rc(i)
    
print(answer)