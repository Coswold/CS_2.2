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
        assert vertex.getNeighbors() == [8, 3]

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
        pass

