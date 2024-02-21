from Engine.engine import Value

#_______________Using Recursion TEchnique_________________________

def recursive_connection(V):
    nodes = set()
    edges = set()

    def recursive(V):
        if V not in nodes:
            nodes.add(V) 
            for i in V._children:   
                edges.add((i,V))     
                recursive(i)
    recursive(V)
    return nodes,edges
