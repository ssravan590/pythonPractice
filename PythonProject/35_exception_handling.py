print('stmt-1')
try:
 print(1/0)
except BaseException as e:
 print("Exception occured please check", e.__class__.__name__)
 print("Exception occured please check", type(e).__name__)
print('stmt-2')

print('stmt-1')
try:
 x = int(input("Enter 1 digit"))
 y = int(input("enter 2 digit"))
 z = x/y
except ZeroDivisionError as e:
    print("Exception occured please check",e.__class__.__name__)
    print("Exception occured please check", type(e).__name__)
except ValueError as e:
    print("Exception occured please check",e.__class__.__name__)
    print("Exception occured please check", type(e).__name__)
print('stmt-2')