import math
from Engine.propengine import topo_nodes

class Value:

    def __init__(self,data,_op = '',_children = (),label = ''):

        self.data = data
        self._op = _op
        self._children = set(_children)
        self.label = label
        self.grad = 0.0
        self._backward = lambda : None
        
    def __repr__(self):
        
        return f"Value(data = {self.data})"
    

    
     #_________________Instance Compatibility___________________________________
    
    def check_comp(self,other):

        other = Value(other) if not isinstance(other,Value) else other

        return other
    
    
    #______________________Opertions +,-,*,^,/,%________________________________


    #Addition Operation
    def __add__(self,other):

        other = self.check_comp(other)
        out = self.data + other.data
        val = Value(out,'+',(self,other))

        def compute_grads():

            self.grad += 1.0 * val.grad
            other.grad += 1.0 * val.grad
        
        val._backward = compute_grads
        return val
    

    def __radd__(self,other):
        
        return self+other
    
    
    #Mutiplication Operation

    def __mul__(self,other):

        other = self.check_comp(other)
        
        out = self.data * other.data
        val = Value(out,'*',(self,other))

        def compute_grads():
            self.grad +=  other.data * val.grad
            other.grad += self.data * val.grad
        val._backward = compute_grads
        return val

    
    def __rmul__(self,other):
        
        return self*other
    
    
    
    #Subtraction Operation
    def __neg__(self): # -self
        return self * -1

    def __sub__(self,other):
        val = self +(-other)
        return val
    
    #division operation
        
    def __truediv__(self,other):

        other = self.check_comp(other)
        #out = self.data/other.data
        out = self * other ** -1
        return out

    def __rtruediv__(self,other):

        if other is None:
            return self
        else:

            other = self.check_comp(other)
            out = other.data * self.data ** -1
            val = Value(out)
            return val


     #Power Operation
        
    def __pow__(self,other):

        assert isinstance(other,(int,float))
        out = self.data ** other
        val = Value(out,'^',(self,))

        def compute_grads():

            self.grad += (other * self.data ** (other -1 )) * val.grad
        
        val._backward = compute_grads
        return val


    def exp(self):

        x = self.data
        out = math.exp(x)
        val = Value(out,'exp',(self,))

        def compute_grads():
            self.grad += val.data * val.grad
        val._backward = compute_grads

        return val


    #___Non-Linear Fuhnctions_______________________________

    def tanh(self):
        x = self.data
        out = math.tanh(x)
        val = Value(out,'tanhx',(self,))

        def compute_grads():
            self.grad += (1.0 - out** 2) * val.grad
        val._backward = compute_grads

        return val
     

    def backward(self):

        self.grad = 1.0
        topo_nodes(self)

        
        




