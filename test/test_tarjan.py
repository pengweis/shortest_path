import numpy as np
import linecache
import copy
from src.heap import Heap, MinHeap
from collections import defaultdict
from src.ultilities import convert_to_adj_list
from heapq import *


def heap_shortest_path_spanning_tree(adj_dict, root):
    hspst = defaultdict(set) # Initially, create shortest path spanning tree as an empty dict
    visited = set([root]) # Create set of nodes visited with root r
    arcs = [(weight, root, neighbour) for neighbour, weight in adj_dict[root].items()] # Create list neighbours of r
    a = MinHeap(arcs) #shift down neighbours of r as children of r in the heap

    while arcs:
        weight, nodes, neighbour = a.extract_min() # remove and return the smallest element from heap
        if neighbour not in visited: #add neighbours to priority queue
            visited.add(neighbour) #add visited neighbours to the visited set
            hspst[nodes].add(neighbour)
            for neighbour_of_neighbour, weight in adj_dict[neighbour].items():
                if neighbour_of_neighbour not in visited: #add neighbours of neighbours to priority queue
                    a.insert((weight, neighbour, neighbour_of_neighbour))
    print("-------------------------SOLUTION-------------------------")
    print(dict(hspst))


def calculate_distances(graph, starting_vertex):
    distances = {vertex: np.inf for vertex in graph}
    visited = set()
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex), []]
    while len(pq) > 0:
        heap = MinHeap(pq)
        current_distance, current_vertex, path = heap.extract_min()
        if current_vertex not in visited:
            visited.add(current_vertex)
            path = [current_vertex] + path
        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heap.insert((distance, neighbor))

    return distances

