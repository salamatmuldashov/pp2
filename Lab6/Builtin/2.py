def Function(s):
    lower,upper = 0,0
    for char in s:
        if ord(char) >=97 and ord(char) <= 122:
            lower+=1
        elif ord(char) >= 65 and ord(char) <= 90:
            upper+=1

    print("Lower:" + str(lower) + " " + "Upper:" + str(upper))

s = input()
Function(s)