from collections import deque
from .stack import Stack

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

    def count(self):
        return self.dq.count()

class Vertex:
    """
    Input:Value
    What is doing: Store the value
    Return: None
    """

    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        """
        Input: Vertex, weight
        What is doing: Store the vertex and the weight
        Return: None
        """
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
        Input: None
        What is doing: It is creating an empty graph
        Return: None
        """
        self.__adj_list = {}
        self.adjacent_list = self.__adj_list

    def add_node(self, value):
        """
        Input : Value
        What is doing : add node to the Graph
        Return : node
        """
        node = Vertex(value)
        self.__adj_list[node] = []
        return node

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Input: start_vertex, end_vertex , weight:optional
        What is doing: Creat an edge and append the edge to the value of
        start_vertex inside the adj_list
        Return: None
        """
        if start_vertex not in self.__adj_list:
            raise KeyError("Start Vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End Vertex is not found")
        edge = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        """
        Input : Vertex
        What is doing: Get all neighbors for a vertex
        Return: a list of edges
        """
        return self.__adj_list.get(vertex, [])

    def get_nodes(self):
        """
        Input : None
        What is doing : get all the nodes in the graph as a set or list
        Return : a list or set of the nodes
        """
        if len(self.__adj_list.keys()) < 1:
            return None
        return self.__adj_list.keys()

    def size(self):
        """
        Input: None
        What is doing: find the length of the adj_list
        Return: int The size(the length of adj_list)
        """
        return len(self.__adj_list)
    
    def dfs(self, start_vertex):
        stack = Stack()
        result = []
        visited = set()

        stack.push(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)

        while stack.peek():
            current_vertex = stack.pop()
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    stack.push(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor.value)

        return result

    def bfs(self, start_vertex):
        queue = Queue()
        result = []
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)

        while len(queue):
            current_vertex = queue.dequeue()
            neighbors = self.get_neighbors(current_vertex)
    
            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor.value)

        return result


def business_trip(graph, list):
    sum = 0
    for i in range (len(list)-1):
        result = 0
        for edge in graph.get_neighbors(list[i]):
            if edge.vertex == list[i+1]:
                result = edge.weight
                sum += result
        if result == 0:
            return None
    return sum



graph = Graph()
vertex1 = graph.add_node('A')
vertex2 = graph.add_node('B')
vertex3 = graph.add_node('C')
vertex4 = graph.add_node('D')
vertex5 = graph.add_node('E')
vertex6 = graph.add_node('F')
vertex7 = graph.add_node('G')
vertex8 = graph.add_node('H')

graph.add_edge(vertex1, vertex2)
graph.add_edge(vertex1, vertex3)
graph.add_edge(vertex2, vertex4)
graph.add_edge(vertex2, vertex3)
graph.add_edge(vertex2, vertex1)
graph.add_edge(vertex4, vertex1)
graph.add_edge(vertex4, vertex5)
graph.add_edge(vertex4, vertex8)
graph.add_edge(vertex4, vertex6)
graph.add_edge(vertex4, vertex2)
graph.add_edge(vertex6, vertex8)
graph.add_edge(vertex6, vertex4)
graph.add_edge(vertex8, vertex4)
graph.add_edge(vertex8, vertex6)
graph.add_edge(vertex5, vertex4)
graph.add_edge(vertex3, vertex2)
graph.add_edge(vertex3, vertex7)
graph.add_edge(vertex7, vertex3)
print(graph.dfs(vertex1))
