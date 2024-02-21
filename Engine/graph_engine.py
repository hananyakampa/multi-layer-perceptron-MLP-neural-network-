from Engine.node_edge_engine import recursive_connection
from graphviz import Digraph


def graph_trach(L,format='svg', rankdir='LR'):
    _N,_E = recursive_connection(L)        
    dot = Digraph(format=format, graph_attr={'rankdir': rankdir})

    for i in _N:

        uid = str(id(i))

        dot.node(uid , f"{i.label} = Value(data = {i.data: .4f}) | grad = {i.grad:.4f}",shape = 'record',style = "filled", fillcolor = "cyan")  #check for empty space in a string
        if i._op:
            dot.node(uid+i._op  , i._op,style = "filled", fillcolor = "mistyrose") #color attributes : color = ,fillcolor = 
            dot.edge(uid+i._op , uid,style = "filled", fillcolor = "blue")    # ==> in this uid+i._op belongs to line 15 node and uid  belongs to line 13 node

    for e1,e2 in _E:
        dot.edge(str(id(e1)),str(id(e2)) + e2._op,style="filled,dashed", color = "blue")

    return dot.render('Engine\graph_tracing\graph', view=True)



