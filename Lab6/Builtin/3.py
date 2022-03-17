s = input()
t = ""
for char in reversed(s):
    t+=char

if s == t:
    print("Palindrome")
else:
    print("Not Palindrome")