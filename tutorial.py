# while loop 

# spam = 0
# while spam < 5:
#     print('hello world!')
#     spam = spam + 5

# import sys
# print('hello')    
# sys.exit
# print('hel')
# import pyperclip
# pyperclip.copy

def divideby(num):
  try:
    return 42/num
  except ZeroDivisionError:
      print('error: dont divide by zero!')
print(divideby(0))
print(divideby(2))