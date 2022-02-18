def Check(s):
    for i in range(int(len(s)/2)):
        if s[i] == s[len(s)-i-1]:
            return True

    return False
            
        
s = input()
if Check(s):
    print(s + " is Palindrome")
else:
    print(s + " is not Palindrome")