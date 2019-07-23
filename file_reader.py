from graph_adt import Graph

def read(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    # Check first line
    typ = lines[0].strip() if len(lines) > 0 else None
    if typ != 'G' and typ != 'D':
        raise Exception("File must start with G or D")
    biderectional = typ == 'G'

    g = Graph()

    # Add vertices
    for vertex in lines[1].strip('() \n').split(','):
        g.addVertex(vertex)

    # Add edges
    for line in lines[2:]:

        edge = line.strip("() \n").split(',')
        if len(edge) < 2 or len(edge) > 3:
            raise Exception("Edges must contain between 2 and 3 inputs")

        v1 = edge[0]
        v2 = edge[1]

        weight = int(edge[2]) if len(edge) == 3 else None

        g.addEdge(v1, v2, weight)
        if biderectional:
            g.addEdge(v1, v2, weight)

    return g
