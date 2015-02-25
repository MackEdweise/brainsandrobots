import copy

class Stack:

    def __init__(self):
        
        self._values = []
        return

    def __len__(self):
       
        return len(self._values)

    def is_empty(self):
        
        if len(self._values)==0:
            result=True
        else:
            result=False

        return result

    def push(self, value):
        
        self._values.append(copy.deepcopy(value))
        return

    def pop(self):
        
        value=None
        if len(self._values)!=0:
            value=copy.deepcopy(self._values[-1])
            del(self._values[-1])

        return value

    def peek(self):
        
        value=None
        if len(self._values)!=0:
            value=copy.deepcopy(self._values[-1])

        return value

    def print_i(self):
        
        for i in range(len(self._values)):
            print(self._values[i])
        return
    
    def combine(self,s2):
       
        s3=Stack()
        while not (len(self._values)==0 and len(s2)==0):
            if len(self._values)!=0:
                x=self._values.pop(-1)
                s3._values.append(x)
            if len(s2)!=0:
                x=s2._values.pop(-1)
                s3._values.append(x)
        return s3
