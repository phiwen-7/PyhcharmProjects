class Edge():
    def __init__(self, l_node, r_node, weight = 0):
        self.l_node = l_node
        self.r_node = r_node
        self.weight = weight


class Graph():
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.edges = []

        for i in edges:
            print(i)
            self.edges.append(Edge(edges[0], edges[1]))


if __name__ == '__main__':

    v = [1, 2, 3]
    e = [[1, 2], [1, 3], [2, 3]]
    g = Graph (v, e)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
