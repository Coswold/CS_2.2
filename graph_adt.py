#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.visited = False
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if vertex in self.neighbors:
            return
        else:
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjacent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        n = []
        for neighbor in self.neighbors:
            n.append(neighbor)
        return n

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        if vertex not in self.neighbors:
            return None
        return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        vert = Vertex(key)
        if key not in self.vertList:
            self.numVertices += 1
            self.vertList[key] = vert
        return self.vertList[key]

    def getVertex(self, n):
        """return the vertex if it exists"""
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getCost(self, f, t):
        """return the cost of going from f to t"""
        if f not in self.vertList or t not in self.vertList:
            return None
        else:
            return self.vertList[f].getEdgeWeight(self.getVertex(t))

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def FSP(self, f, t):
        short_path = []
        self.BFS(f, t, short_path.append)
        return short_path

    def BFS(self, f, t, visit, q=[]):
        neighbors = self.getVertex(f).getNeighbors()
        q.append(f)
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if neighbor.getId() == t:
                    visit(q)
                    return
                self.BFS(neighbor.getId(), t, visit, q)
        else:
            raise Exception("Path not found")

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use syntax: for v in g
        """
        return iter(self.vertList.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Friend 1")
    g.addVertex("Friend 2")
    g.addVertex("Friend 3")
    g.addVertex("Friend 4")
    g.addVertex("Friend 5")
    g.addVertex("Friend 6")
    g.addVertex("Friend 7")
    g.addVertex("Friend 8")
    g.addVertex("Friend 9")
    g.addVertex("Friend 10")


    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Friend 1", "Friend 2")
    g.addEdge("Friend 2", "Friend 3")
    g.addEdge("Friend 3", "Friend 4")
    g.addEdge("Friend 4", "Friend 5")
    g.addEdge("Friend 5", "Friend 6")
    g.addEdge("Friend 6", "Friend 7")
    g.addEdge("Friend 7", "Friend 8")
    g.addEdge("Friend 8", "Friend 9")
    g.addEdge("Friend 9", "Friend 10")
    g.addEdge("Friend 1", "Friend 8")

    # BFS test
    print(g.FSP('Friend 1', 'Friend 8'))

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", "\n")
    for vert in g.getVertices():
        print(vert)
    print("\n")

    print("The edges are: ", "\n")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))

