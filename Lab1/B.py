s = input()
sum = 0
for i in range(0,len(s)):
    sum+=ord(s[i])

if sum <= 300:
    print("Oh, no!")
else:
    print("It is tasty!")