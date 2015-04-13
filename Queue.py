
import copy

class Queue:

    def __init__( self ):
      
        self._values = []
        return

    def __len__( self ):
        
        return len( self._values )

    def is_empty( self ):
        
        return len( self._values ) == 0

    def insert( self, value ):
        
        
        self._values.append(copy.deepcopy(value))
        
        return

    def remove( self ):
       
        if len(self._values)==0:
            value=None
        else:
            value=copy.deepcopy(self._values[0])
            del(self._values[0])
        
        return value

    def peek( self ):
        
        if len(self._values)!=0:
            value=copy.deepcopy(self._values[0])
        else:
            value=None
        
        return value

    def print_i( self ):
      
        for i in range( len( self._values ) ):
            print( self._values[i] )
        return

    def split(self):
       
        q2=Queue()
        q3=Queue()
        while not len(self._values)==0:
            q2._values.append(copy.deepcopy(self._values[0]))
            del self._values[0]
            q3._values.append(copy.deepcopy(self._values[0]))
            del self._values[0]
            
        return q2, q3
