from src.heap import Heap, MinHeap
from src.ultilities import convert_to_adj_list
import numpy as np


def TarjanSPathTree(graph, starting_node):

    solution_dict = {}

    for ending_node in graph.keys():
        pq, visited, distance = [(0, starting_node, [])], set(), {starting_node: 0}
        while pq:
            heap = MinHeap(pq)
            (cost, current_node, path) = heap.extract_min()
            if current_node not in visited:
                visited.add(current_node)
                path = [current_node] + path
                if current_node == ending_node:
                    solution_dict[ending_node] = (cost, path)

                for neighbor, weight in graph.get(current_node, ()):
                    if neighbor in visited:
                        continue
                    prev = distance.get(neighbor, None)
                    next = cost + weight
                    if prev is None or next < prev:
                        distance[neighbor] = next
                        heap.insert((next, neighbor, path))

    return solution_dict


def find_shortest_path_bt_two_nodes(graph, starting_node, ending_node):

    pq, visited, distance = [(0, starting_node, [])], set(), {starting_node: 0}
    while pq:
        heap = MinHeap(pq)
        (cost, current_node, path) = heap.extract_min()
        if current_node not in visited:
            visited.add(current_node)
            path = [current_node] + path
            if current_node == ending_node:
                return cost, path

            for neighbor, weight in graph.get(current_node, ()):
                if neighbor in visited:
                    continue
                prev = distance.get(neighbor, None)
                next = cost + weight
                if prev is None or next < prev:
                    distance[neighbor] = next
                    heap.insert((next, neighbor, path))

    return np.inf, []


if __name__ == "__main__":

    file = "../data/ballyskate_layout.txt"
    graph = convert_to_adj_list(file)
    print(graph)
    print(TarjanSPathTree(graph, '1'))
    print(find_shortest_path_bt_two_nodes(graph, '1', 'p'))