"""
Prim's algorithm reveals a minimum spanning tree of 
a weighted undirected graph.
"""

class Graph:
    def __init__(self) -> None:
        self.vertices = {}

    def print_graph(self) -> None:
        """Prints a visual representation of the graph."""

        print(self.vertices)
        for vertex in self.vertices:
            print(vertex, " : ", " -> ".join([str(adj) for adj in self.vertices[vertex]]))

    def add_edge(self, start_vertex, end_vertex) -> None:
        """Adds an edge between two vertices."""

        if start_vertex in self.vertices:
            # Vertex is already present
            self.vertices[start_vertex].append(end_vertex)
        else:
            # Create a list with the vertex
            self.vertices[start_vertex] = [end_vertex]

    """ The Algorithm Design Manual Pseudocode
    prim(G)
        select an arbitrary vertex s to start the tree from
        while there are still nontree vertices
            select the edge of minimum weight between a tree and nontree vertex
            add the selected edge and vertex to the tree
    """

    """ Algorithms Pseudocode
    prim(G,weights)
        for all vertices u in the graph
            cost[u] = infinity
            prev[u] = nil
        pick any initial vertex s
        cost[s] = 0

        H = makequeue(V)    (priority queue, using cost-values as keys)
        while H is not empty
            v = deletemin(H)
            for all edges (v,z)
                if cost[z] > weight(v,z)
                    cost[z] = weight(v,z)
                    prev[z] = v
                    decreasekey(H,z)
    """