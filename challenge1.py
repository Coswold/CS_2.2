import sys
from graph_adt import Graph

def read(txt):
    f = open(txt, "r")
    txt = f.read().split('\n')
    txt.pop()
    return txt

def buildGraph(txt):
    g = Graph()
    verts = txt[1]
    verts = verts.split(',')
    for vert in verts:
        g.addVertex(vert)

    return g


if __name__ == '__main__':
    if len(sys.argv) > 1:
        txt = read(sys.argv[1])
        print(txt)
        g = buildGraph(txt)
