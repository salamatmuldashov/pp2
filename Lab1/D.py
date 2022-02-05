x = int(input())
y = input()
if y == 'k':
    z = int(input())
    print(round(x / 1024,z))

else:
    print(x * 1024)