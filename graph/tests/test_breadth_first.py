from graph.graph import Graph
import pytest


def test_breadth_first(graph):
    expected = [1,2,3,4]
    actual = graph.bfs(vertex1)
    assert expected == actual

def test_breadth_first2(graph2):
    expected = [1]
    actual = graph2.bfs(vertex2)
    assert expected == actual

def test_breadth_first_empty(graph2):
    graph = Graph()
    with pytest.raises(TypeError):
        graph.bfs()

@pytest.fixture
def graph():
    graph = Graph()
    global vertex1
    vertex1 = graph.add_node(1)
    vertex2 = graph.add_node(2)
    vertex3 = graph.add_node(3)
    vertex4 = graph.add_node(4)
    graph.add_edge(vertex1, vertex2)
    graph.add_edge(vertex1, vertex3)
    graph.add_edge(vertex1, vertex4)
    return graph

@pytest.fixture
def graph2():
    graph2 = Graph()
    global vertex2
    vertex2 = graph2.add_node(1)
    return graph2
    