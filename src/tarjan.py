import numpy as np
import linecache
import copy
from src.heap import Heap


class TarjanSPathTree:

    def __init__(self, network, root=1):
        self.network = network
        self.matrix = np.loadtxt(self.network, skiprows=2)
        self.matrix[self.matrix == 0] = np.inf
        self.node_num = int(linecache.getline(self.network, 2))
        """
        root is the rank of the root
        root code is the python rank of the root
        root name is the actual name of the root
        """
        self.root = root
        self.root_code = root - 1
        self.permanent_set = []
        self.temporary_set = [*range(0, self.node_num)]
        self.distance_heap = Heap()
        self.adj_set = set()
        self.permanent_set_alternative = [] # for betweenness centrality recording every other shorteset path
        self.permanent_set_all = [] # recording every shortest path in insert order
        self.path = [0] # for get_path

    def algorithm(self):
        matrix = self.matrix
        self.distance_heap.Insert(
            [self.root_code, 0, self.root_code])  # [node_index, distance from parent, parent]

        while self.distance_heap.heap_list:
            node_u = self.distance_heap.heap_list[0][0]
            # get new permanent node

            node_u, sp_distance, sp_parent = self.distance_heap.DeleteMin()
            # update permanent_set
            self.permanent_set.append([node_u, sp_distance, sp_parent])
            self.permanent_set_all.append([node_u, sp_distance, sp_parent])
            # make sure no same node and distance

            while self.distance_heap.heap_list and any([i[0] == node_u for i in self.distance_heap.heap_list]):
                index_parent = get_bool_index([k[0] == node_u for k in self.distance_heap.heap_list], True)
                for index, i in enumerate(index_parent):
                    # get new permanent node
                    self.distance_heap.equal_Siftup(i-index)
                    node_u, sp_distance, sp_parent = self.distance_heap.DeleteMin()

                    # update permanent_set s
                    self.permanent_set_alternative.append([node_u, sp_distance, sp_parent])
                    self.permanent_set_all.append([node_u, sp_distance, sp_parent])

            # update temporary_set
            self.temporary_set.remove(node_u)

            # update adj_list
            old_adj_set = copy.deepcopy(self.adj_set)
            if node_u == 9:
                print(self.matrix[node_u])
                print(np.where(np.isinf(self.matrix[node_u]) == 0))
            new_adj_set = set(np.where(np.isinf(self.matrix[node_u]) == 0)[0])

            for i in new_adj_set:
                self.adj_set.add(i)
            self.adj_set = {x for x in self.adj_set if x in self.temporary_set}
            print(self.adj_set)
            # relax inequality and update heap
            for i in self.adj_set:
                new_adj_path = matrix[node_u][i] + self.permanent_set[-1][1]
                if i not in old_adj_set:
                    self.distance_heap.Insert([i, new_adj_path, node_u])
                else:
                    old_adj_path = self.distance_heap.get_info(i)
                    if old_adj_path[1] == new_adj_path:
                        self.distance_heap.Insert([i, new_adj_path, node_u])
                    if old_adj_path[1] > new_adj_path:
                        old_adj_path[2] = node_u
                        # self.distance_heap.heap_list
                        old_adj_path[1] = new_adj_path
                        self.distance_heap.SiftUp(self.distance_heap.get_index(i))

        # print(self.permanent_set)
        # print(self.permanent_set_alternative)

    def closeness(self):
        closeness_list = []
        for i in range(self.node_num):
            self.__init__(self.network, i + 1)
            self.algorithm()
            closeness_list.append(sum(i[1] for i in self.permanent_set) / (self.node_num - 1))
        return np.array(closeness_list)

    def get_path(self):
        outcomewith_path = self.permanent_set_all
        # outcomewith_path = self.permanent_set # get one
        outcomewith_path[0].append([])
        outcomewith_path[0][3].append([])
        # get node list in insert order
        ordered_nodes = [i[0] for i in self.permanent_set_all]
        for index_all, i in enumerate(ordered_nodes):
            if i == self.root_code:
                continue
            # get node's parent's path
            parent = self.permanent_set_all[index_all][2]
            index_parent = get_bool_index([k[0] == parent for k in outcomewith_path], True)
            # index_parent = [k[0] == parent for k in outcomewith_path].index(True)
            outcomewith_path[index_all].append([])

            for k in index_parent:
                for path in outcomewith_path[k][3]:
                    parent_path = copy.deepcopy(path)
                    parent_path.append(parent)

                    # update into the forth element of the node with its parent's path and its parent itself
                    outcomewith_path[index_all][3].append(parent_path)

        return outcomewith_path

    def betweenness(self):
        self.permanent_set

    def __get_path_assistance__(self, node):
        while node:
            node = self.permanent_set[node][2]
            self.path.append(node)

            self.__get_path_assistance__(node)