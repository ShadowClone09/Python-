
#Guess a random number

import random

u = int(input("Set a range. Guess from "))

v = int(input(" to "))

a = random.randint(u, v)

print("I have guessed a number.")

n = int(input("How many chances do you want?"))

print("Guess the number now.")

i = 0

while i < n:

    i = i + 1

    b = int(input())

    if b == a:

        print("Correct!!")

        print("The number was " + str(a), ".")

        break

    elif b - a > 2:

        print("Too high!!")


    elif b - a < -2:

        print("Too low!!")


    elif b - a <= 2:

        print("Almost there...")


    elif b - a <= -2:

        print("Almost there...")

    if i == n:

        print("You're out of chances!")
        
        print("The number was " + str(a), ".")
        
        break

p = i - 1

#if p > 0:
    #print("The number was " + str(a))

q = 10 - p

print("You scored " + str(q), "points.")











