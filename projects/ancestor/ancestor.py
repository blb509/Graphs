from util import Stack, Queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        graph.add_edge(ancestor[1], ancestor[0])
    if graph.vertices[starting_node] == set():
        return -1
    s = Stack()
    earliest_ancestor = []
    s.push([starting_node])
    while s.size() > 0:
        path = s.pop()
        vertex = path[-1]
        if len(path) > len(earliest_ancestor):
            earliest_ancestor = path
        if len(path) == len(earliest_ancestor) and path[-1] < earliest_ancestor[-1]:
            earliest_ancestor = path
        for neighbor in graph.vertices[vertex]:
            newPath = path.copy()
            newPath.append(neighbor)
            s.push(newPath)
    return earliest_ancestor[-1]
