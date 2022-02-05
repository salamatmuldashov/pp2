def toLowercase(s):
    answer = ""
    for character in s:
        if (character >= 'A' and character <= 'Z'):
            answer+=chr(ord(character)+32)
        else:
            answer+= character

    print(answer)
            
            

s = input()
toLowercase(s)
