class YoungException(Exception):
    def __init__(self,msg):
        self.msg = msg

class OldException(Exception):
    def __init__(self,msg):
        self.msg = msg
try:
 age = int(input('enter age :'))
 if age > 60:
    raise OldException("I am old")
 else:
    raise YoungException("I am young")
except Exception as e:
 print(" I caugt :",e)

