#Multi layer perceptron
from Engine.engine import Value
import random
from Engine.graph_engine import graph_trach


class SingleNeuron:
    
    def __init__(self,dim_input):
        
        self.b = Value(random.uniform(-1,1))

        self.w  = []

        for _ in range(dim_input):

            rw = random.uniform(-1,1)  

            rw = Value(rw)

            self.w.append(rw)

    def __call__(self,x):
        
        wixi = self.b

        #print(wixi)

        #print('_____________________________________')

        for i,j in zip(self.w,x):
            
            wixi += i*j

            #print('wixi = ',wixi)

        out = wixi.tanh()

        return out
    
    def parameters(self):
        return self.w + [self.b]
    
class MultipleNeurons:
    
    def __init__(self,nin,nout):
        
        self.neurons = []

        for _ in  range(nout):
            
            self.neurons.append(SingleNeuron(nin))

    def __call__(self,x):
        
        out = [n(x) for n in self.neurons]

        return out[0] if len(out) == 1 else out
    
    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]
    
class MLP:
  
  def __init__(self, nin, nouts):
    sz = [nin] + nouts
    self.layers = [MultipleNeurons(sz[i], sz[i+1]) for i in range(len(nouts))]
  
  def __call__(self, x):
    for layer in self.layers:
       x = layer(x)
    return x
  
  def parameters(self):
      return [p for layer in self.layers for p in layer.parameters()]
  


#x =[2.0,3.0,-1.0]
#n = MLP(len(x),[4,4,1])

#s = len(x)

#L = MultipleNeurons(s,3)

#print(n(x))

#graph_trach(n(x))



xs = [
  [2.0, 3.0, -1.0],
  [3.0, -1.0, 0.5],
  [0.5, 1.0, 1.0],
  [1.0, 1.0, -1.0],
]
ys = [1.0, -1.0, -1.0, 1.0] # desired targets#

n = MLP(len(xs[0]),[4,4,1])

'''
ypred = [n(x) for x in xs]
print(ypred)


loss = sum([(yp-yt)**2 for yt,yp in  zip(ys,ypred)])
print('loss = ',loss)

loss.backward()

graph_trach(loss)
'''

for k in range(20):
  
  # forward pass
  ypred = [n(x) for x in xs]
  loss = sum((yout - ygt)**2 for ygt, yout in zip(ys, ypred))
  
  # backward pass
  for p in n.parameters():
    p.grad = 0.0
  loss.backward()
  
  # update
  for p in n.parameters():
    p.data += -0.1 * p.grad
  
  print(k, loss.data)
  

graph_trach(loss)