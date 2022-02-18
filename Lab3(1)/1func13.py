import random
flag = False
cnt = 0
number = random.randrange(1,21)
print(number)
print()
print("Hello! What is your name?")
s = input()
print()
print("Well, " + s + "," + " I am thinking of a number between 1 and 20.")
print("Take a guess.")
while flag != True:
    x = int(input())
    print()
    if x < number:
        print("Your guess is too low")
        print("Take a guess.")
        cnt+=1
    elif x > number:
        print("Your guess is too high")
        print("Take a guess.")
        cnt+=1
    else:
        print("Good job, " + s + "!" + " You guessed my number in " + str(cnt) + " guesses!")
        flag = True




