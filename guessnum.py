import random

print('Hello whats your name')
name = input()

print('Hello ' + name + '! predict the number im thinking between 1-20')
secret = random.randint(1, 20)
# print(secret) line to debug

for guesstaken in range(1, 6):
    print('take a guess')
    num = int(input())
    if num > secret:
     print('ohoh, Its more than i think !')
    elif num < secret:
     print('ohoh! its less than i think')
    else:
     break

if num == secret:
    print('you guessed right ! At ' + str(guesstaken) + 'guesses')
else:
    print('the number i was thinking was ' + str(secret))