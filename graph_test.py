#!python

from graph_adt import Vertex, Graph
import unittest


class VertexTest(unittest.TestCase):

    def test_init(self):
        data = 123
        vertex = Vertex(data)
        assert vertex.id is data

    def test_add_neighbor(self):
        vertex = Vertex(1)
        vertex.addNeighbor(3)
        assert vertex.neighbors[3] == 0

    def test_get_neighbors(self):
        vertex = Vertex(1)
        vertex.addNeighbor(3)
        vertex.addNeighbor(8)
        assert 8 in vertex.getNeighbors()
        assert 3 in vertex.getNeighbors()

    def test_get_id(self):
        vertex = Vertex(1)
        vertex.addNeighbor(3)
        assert vertex.getId() == 1

    def test_get_edge_weight(self):
        vertex = Vertex('A')
        vertex.addNeighbor('B', 5)
        assert vertex.getEdgeWeight('B') == 5


class GraphTest(unittest.TestCase):

    def test_init(self):
        graph = Graph()
        graph.numVertices = 0

    def test_add_vertex(self):
        graph = Graph()
        assert graph.addVertex('A') == graph.vertList['A']
        assert graph.numVertices == 1
        graph.addVertex('B')
        assert graph.numVertices == 2

    def test_get_vertex(self):
        graph = Graph()
        graph.addVertex('A')
        graph.addVertex('B')
        assert graph.getVertex('A') is graph.vertList['A']
        assert graph.getVertex('B') is graph.vertList['B']
        assert graph.getVertex('C') is None

    def test_add_edge(self):
        graph = Graph()
        graph.addVertex('A')
        graph.addVertex('B')
        graph.addEdge('A', 'B', 8)
        assert graph.getVertex('A').getEdgeWeight(graph.getVertex('B')) == 8
        graph.addEdge('B', 'C', 5)
        assert graph.getVertex('B').getEdgeWeight(graph.getVertex('C')) == 5
        graph.addEdge('D', 'E', 10)
        assert graph.getVertex('D').getEdgeWeight(graph.getVertex('E')) == 10

    def test_get_cost(self):
        graph = Graph()
        graph.addVertex('A')
        graph.addVertex('B')
        graph.addEdge('A', 'B', 8)
        assert graph.getCost('A', 'B') == 8
        assert graph.getCost('A', 'C') is None

    def test_BFS(self):
        g =Graph()
        g.addVertex('A')
        g.addVertex('B')
        g.addVertex('C')
        g.addVertex('D')
        g.addVertex('E')
        g.addEdge('A', 'B', 2)
        g.addEdge('B', 'C', 6)
        print(g.BFS('A', 'C'))
        assert g.BFS('A', 'C') == ['A', 'B', 'C']
