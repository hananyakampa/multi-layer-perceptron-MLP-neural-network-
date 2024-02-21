#_________________________Topological Sorting________________________________

def topo_nodes(start):
    topo = []
    visited_nodes = set()

    def build_topo(v):
            
        if v not in visited_nodes:
            visited_nodes.add(v)
            for i in v._children:
                build_topo(i)
            topo.append(v)
            
    build_topo(start)
    start.grad = 1.0
    for node in reversed(topo):       
        
        node._backward()

        
