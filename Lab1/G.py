def Dec(s):
    if (s == 0):
        return 0
    else:
        return (s % 10 + 2 * Dec(s // 10))


s = int(input())
print(Dec(s))

