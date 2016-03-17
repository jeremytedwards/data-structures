# coding=utf-8

import pytest


@pytest.fixture(scope='function')
def g():
    from simpleg import Graph
    return Graph()


def test_nodes(g):
    assert set(g.nodes()) == set()
    for i in range(5):
        g.add_node(i)
    assert set(g.nodes() == set(range(5)))


def test_edges(g):
    assert set(g.edges()) == set()
    for i in range(5):
        g.add_node(i)
    for i in range(5):
        g.add_edge(i, (i + 1) % 5)
    assert set(g.edges()) == {
        (i, (i + 1) % 5)
        for i in range(5)
    }


# def test_add_node(g):
#     this test is covered by test_nodes


# def test_add_edge(g):
#     this test is covered by test_edges


def test_del_node(g):
    for i in range(5):
        g.add_node(i)
    assert g.has_node(3)
    g.del_node(3)
    assert not g.has_node(3)
    with pytest.raises(KeyError):
        g.del_node(3)


def test_del_edge(g):
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    assert g.adjacent(1, 2)
    g.del_edge(1, 2)
    assert not g.adjacent(1, 2)
    with pytest.raises(KeyError):
        g.del_edge(1, object())
    with pytest.raises(KeyError):
        g.del_edge(object(), 2)


def test_has_node(g):
    assert not g.has_node(1)
    g.add_node(1)
    assert g.has_node(1)


def test_neighbors(g):
    for i in range(5):
        g.add_node(i)
    for i in range(1, 5):
        g.add_edge(0, i)
    assert set(g.neighbors(0)) == set(range(1, 5))
    with pytest.raises(KeyError):
        g.neighbors(object())


def test_adjacent(g):
    for i in range(3):
        g.add_node(i)
    g.add_edge(1, 2)
    assert g.adjacent(1, 2)
    assert not g.adjacent(1, 0)
    assert not g.adjacent(2, 1)
    with pytest.raises(KeyError):
        g.adjacent(1, object())
    with pytest.raises(KeyError):
        g.adjacent(object(), 2)