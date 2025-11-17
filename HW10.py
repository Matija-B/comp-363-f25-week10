def khan(graph: list[list[int]]) -> list[int]:

    """Comprehensive implementation of Kahn's algorithm for topological sorting."""

    # Data integrity check - a bit much but I was having fun with it.
    if (
         graph is None
        or not isinstance(graph, list)
        or len(graph) == 0
        or not all(isinstance(row, list) for row in graph)
        or not all(len(row) == len(graph) for row in graph)
    ):
        raise ValueError("Input must be a non-empty square adjacency matrix.")

    # Ease of reference
    N = len(graph)
    NO_EDGE = graph[0][0]

    # Calculate in-degrees of all vertices.
    in_degrees = [0] * N
    for u in range(N):
        for v in range(N):
            if graph[u][v] != NO_EDGE:
                # In edge u --> v we compute the in-degree of v
                in_degrees[v] += 1

    # Initialize list of source vertices
    sources = []
    for i in range(N):
        if in_degrees[i] == 0:
            sources.append(i)

    # List to store the topological order
    topological_order = []

    # Progressively remove sources and update in-degrees
    while len(sources) > 0:
        # Remove a source vertex
        vertex = sources.pop(0)
        # Add it to the topological order
        topological_order.append(vertex)
        # Decrease in-degrees of its neighbors
        for neighbor in range(N):
            if graph[vertex][neighbor] != NO_EDGE:
                in_degrees[neighbor] -= 1
                # If in-degree becomes zero, add it to sources
                if in_degrees[neighbor] == 0:
                    sources.append(neighbor)

    # Done
    return topological_order

def DFS(G, v, marked):
    # Mark the current vertex as visited
    marked.append(v)
    # Consider all the neighbors of v
    for w in range(len(G)):
        # For any edg v --> w, if w is unmarked,
        # plan to visit it.
        if G[v][w] != G[0][0] and w not in marked:
            # Plan to visit w
            DFS(G, w, marked)
    return marked

def DFS_helper(G, v):
    """Helper method to launch a DFS from vertex v."""
    # Launch DFS from v with empty marked list
    return DFS(G, v, [])

def topoSort (G):
    
    n = len(G)
  
    visited = [0] * n
    completeOrder = []
    
    for v in range(n):
        #We check if vertex is not visted 
        if visited[v] == 0: 
            #Then we want to call our DFS_Helper method.
            local = DFS_helper(G, v)
            #Then we want to traverse the elements that are in local
            #in reverse order
            for u in reversed(local):
                #we again check if not visted
                if visited[u] == 0:
                    #if it is we want to add u in 
                    #our empty list
                    completeOrder.append(u)
                    #then make visted at index u 
                    #one
                    visited[u] = 1 
    #then we want to reverse the list
    finalOrder = list(reversed(completeOrder))
    return finalOrder



G1 = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

G2 = [
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 1, 2, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

order = topoSort(G1)
print(order)
khanOrder = khan(G1)
print(khanOrder)
order2 = topoSort(G2)
print(order2)
khanOrder2 = khan(G2)
print(khanOrder2)