from graph.graph import Graph
import pytest

def test_depth_first(graph):
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = graph.dfs(vertex1)
    assert expected ==  actual

def test_depth_first_one_element():
    graph = Graph()
    vertex1 = graph.add_node('A')
    expected = ['A']
    actual = graph.dfs(vertex1)
    assert expected ==  actual

def test_depth_first_empty():
    graph = Graph()
    with pytest.raises(TypeError):
        graph.dfs()


@pytest.fixture
def graph():
    graph = Graph()
    global vertex1
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
    return graph