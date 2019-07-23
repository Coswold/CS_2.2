import sys
from graph_adt import Graph
from file_reader import read

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
    if len(sys.argv) > 3:
        g = read(sys.argv[1])
        start = sys.argv[2]
        end = sys.argv[3]
        printData(g)
    else:
        raise Exception("Please include text file")
