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
    i = 2
    while i < len(txt):
        g.addEdge(txt[i][1], txt[i][3])
        i += 1

    return g

def printData(g):
    print('# Vertices: {}'.format(g.numVertices))
    print("The vertices are: ", "\n")
    for vert in g.getVertices():
        print(vert)
    print("\n")

    print("The edges are: ", "\n")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        txt = read(sys.argv[1])
        g = buildGraph(txt)
        printData(g)
