#!python

from graph_adt import Vertex, Graph
import unittest


class VertexTest(unittest.TestCase):

    def test_init(self):
        data = 123
        vertex = Vertex(data)
        assert vertex.id is data
        assert vertex.neighbors is {}

    def test_add_neighbor(self):
        vertex = Vertex(1)
        vertex.addNeighbor(3)

    def test_get_neighbors(self):


    def test_get_id(self):


    def test_get_edge_weight(self):


class GraphTest(unittest.TestCase):

    def test_init(self):

