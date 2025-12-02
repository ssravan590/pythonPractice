print('stmt-1')
try:
 x = int(input("Enter 1 digit"))
 y = int(input("enter 2 digit"))
 z = x/y
except (ZeroDivisionError,ValueError) as e:
    print("Exception occured please check",e.__class__.__name__)
    print("Exception occured please check", type(e).__name__)
except:
 print("Default Exception occured please check")
finally:
 print("I am executing finally")

print('stmt-2')