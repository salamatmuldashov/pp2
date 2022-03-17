a = list(map(str,input().split()))
file = open('1234.txt', 'w')
for items in a:
    file.write(items+'\n')


file.close()