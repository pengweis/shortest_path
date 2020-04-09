import networkx as nx

dense_graph = nx.barabasi_albert_graph(200, 150)
sparse_graph = nx.barabasi_albert_graph(200, 10)

if __name__ == "__main__":
    print(dense_graph)
