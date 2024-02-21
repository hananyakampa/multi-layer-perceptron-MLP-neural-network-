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

#_N,_E = recursive_connection(o)

#print(_N)
#print(_E)

#_______________Using stack_________________________

def rootnode(rn):
    nodes,edges= set(),set()
    stack = [rn]

    print(stack)
    
    while stack:
        current_node = stack.pop()
        
        if current_node not in nodes:
            nodes.add(current_node)
            
            for child in current_node._children:
                edges.add((child,current_node))
                stack.append(child)
    
    return nodes, edges

#_N,_E = rootnode(o)

#print(_N)
#print(_E)


#_______________depth-first search (DFS) algorithm_________________________

'''It looks like you have implemented a depth-first search (DFS) algorithm to traverse a graph 
starting from a given root node (rn). The function rootnode_set_visited returns a set of visited 
nodes (nodes) and edges (edges), assuming that the graph is represented by nodes with a _children attribute.

A few things to note:

It seems like the edges set is defined but not used within the function. 
If you intend to store edges, you may want to update the code to include the relevant information.
The line stack.extend(current_node._children - visited) assumes that _children is a set-like object. 
If _children is not a set, you might need to convert it to a set using set(current_node._children).
The code might raise an error if _children contains elements that are not hashable. Ensure that the elements
in _children are hashable, as sets in Python require their elements to be hashable.

'''

        
def rootnode_set_visited(rn):
    nodes = set()
    edges = set()

    stack = [rn]
    visited = set()

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            nodes.add(current_node)

            # Assuming _children is a set of neighboring nodes
            neighbors = current_node._children - visited

            stack.extend(neighbors)

            # Adding edges for each visited neighbor
            edges.update((current_node, neighbor) for neighbor in neighbors)

    return nodes, edges

# Assuming 'o' is your root node
#_N, _E = rootnode_set_visited(o)

#print("Visited Nodes:", _N)
#print("Edges:", _E)



#_______________depth-first search (DFS) algorithm using generators_________________________


def rootnode_set_visited_generator(rn):
    visited = set()

    stack = [rn]

    def dfs():
        while stack:
            current_node = stack.pop()

            if current_node not in visited:
                visited.add(current_node)
                yield current_node

                # Assuming _children is a set of neighboring nodes
                stack.extend(neighbor for neighbor in current_node._children if neighbor not in visited)

    nodes = set(dfs())
    edges = set((current_node, neighbor) for current_node in nodes for neighbor in current_node._children if neighbor in nodes)

    return nodes, edges

# Assuming 'o' is your root node
#_N, _E = rootnode_set_visited_generator(o)

#print("Visited Nodes:", _N)
#print("Edges:", _E)

