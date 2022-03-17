import time
import math
def Function(number,ms):
    time.sleep(ms/1000)
    return math.sqrt(number)
print("Sample Input:")
number = int(input())
ms = int(input())
print("Sample Output:")
print("Square root of " + str(number) + " after " + str(ms) + " milliseconds is " + str(Function(number,ms)))
