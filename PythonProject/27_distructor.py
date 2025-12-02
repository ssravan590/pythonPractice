import time


class DestructorDemo:
    def __init__(self):
        print("I am contructor")
    def __del__(self):
        print("I am destructor")

d = DestructorDemo()
#d=None
del d
time.sleep(100)
print("end of application")