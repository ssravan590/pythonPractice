name="I am from test1.py file"

print("test1 is executed")
print(__name__)


def sum(a,b):
    print("sum from test1")
    return a+b


def mul(a,b):
    print("mul from test1")
    return a*b


if __name__ == '__main__':
    print("i am main and direct executed")
    sum(10,20) # calling will be executed only for main and not for indirect
else:
    print("i am indirect executed by some module")




