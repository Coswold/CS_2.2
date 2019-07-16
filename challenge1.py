import sys
from graph_adt import Graph

def buildGraph(txt):
    f = open(txt, "r")
    for line in f:
        print(line)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        buildGraph(sys.argv[1])
