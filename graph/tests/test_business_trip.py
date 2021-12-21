from graph.graph import Graph, business_trip

def test_business_trip():
    graph = Graph()
    vertex1 = graph.add_node('Pandora')
    vertex2 = graph.add_node('Arendelle')
    vertex3 = graph.add_node('Metropolis')
    vertex4 = graph.add_node('Metrovill')
    graph.add_edge(vertex1, vertex2, 150)
    graph.add_edge(vertex2, vertex3, 42)
    graph.add_edge(vertex3, vertex4, 105)
    list = [vertex1, vertex2, vertex3]

    expected = 192
    actual = business_trip(graph, list)
    assert expected == actual

def test_business_trip_none():
    graph = Graph()
    vertex1 = graph.add_node('Pandora')
    vertex2 = graph.add_node('Arendelle')
    vertex3 = graph.add_node('Metropolis')
    vertex4 = graph.add_node('Metrovill')
    graph.add_edge(vertex1, vertex2, 150)
    graph.add_edge(vertex2, vertex3, 42)
    graph.add_edge(vertex3, vertex4, 105)
    list = [vertex1, vertex2, vertex4]

    expected = None
    actual = business_trip(graph, list)
    assert expected == actual

def test_business_trip_long_trip():
    graph = Graph()
    vertex1 = graph.add_node('Pandora')
    vertex2 = graph.add_node('Arendelle')
    vertex3 = graph.add_node('Metropolis')
    vertex4 = graph.add_node('Metrovill')
    graph.add_edge(vertex1, vertex2, 150)
    graph.add_edge(vertex2, vertex3, 42)
    graph.add_edge(vertex3, vertex4, 105)
    list = [vertex1, vertex2, vertex3, vertex4]

    expected = 297
    actual = business_trip(graph, list)
    assert expected == actual

def test_business_trip_not_connected():
    graph = Graph()
    vertex1 = graph.add_node('Pandora')
    vertex2 = graph.add_node('Arendelle')
    vertex3 = graph.add_node('Metropolis')
    vertex4 = graph.add_node('Metrovill')
    list = [vertex1, vertex2, vertex3, vertex4]

    expected = None
    actual = business_trip(graph, list)
    assert expected == actual
 