import numpy as np
import matplotlib.pyplot as plt
import linecache


class DijkstraSPathTree:
    def __init__(self, network, root=1):
        self.network = network
        self.matrix = np.loadtxt(self.network, skiprows=2); self.matrix[self.matrix == 0] = np.inf
        self.node_num = int(linecache.getline(self.network, 2))
        """
        root is the rank of the root
        root code is the python rank of the root
        root name is the actual name of the root
        """
        self.root = root; self.root_code = root - 1
        self.permanent_set = [self.root_code]
        self.temporary_set = [*range(0, self.node_num)]; self.temporary_set.remove(self.root_code)
        self.parent_set = [self.root_code] * self.node_num
        self.distance_set = self.matrix[self.root_code]
        self.adj_set = set(np.where(np.isinf(self.distance_set) == 0)[0])  # array into set
        self.distance_shortest_set = [0]
        self.parent_shortest_set = [0]

    def visualisation(self):
        """
        visualisation of the network and the outcome
        :return:
        """
        pass

    def algorithm(self):
        matrix = self.matrix
        self.matrix[:, self.root_code] = np.inf

        """
        initialise
        """
        # TODO root shouldn't larger than node_nums/ maybe could input node names

        # TODO validate matrix length
        # node_num_matrix = len(matrix)
        # TODO complexity
        # permanent_set = {1: 1} # with parent node
        # node_names = []

        while self.temporary_set:

            # Select the min distance from the permanent set
            sp_distance = np.min(self.distance_set[list(self.adj_set)])
            self.distance_shortest_set.append(sp_distance)
            node_u = np.where(self.distance_set == sp_distance)[0][0]  # TODO adj or tem
            self.parent_shortest_set.append(self.parent_set[node_u])

            # Delete the node found above from the tem_set and add it to the per_set
            self.permanent_set.append(node_u)
            self.temporary_set.remove(node_u)

            # update adj_set
            new_adj_set = list(np.where(np.isinf(self.matrix[node_u]) == 0)[0])
            for i in new_adj_set:
                self.adj_set.add(i)
            self.adj_set = {x for x in self.adj_set if x in self.temporary_set}

            # update the matrix
            matrix[:, node_u] = np.inf

            # update parent_set and distance_set
            for i in self.adj_set:
                new_adj_path = matrix[node_u][i] + sp_distance
                if self.distance_set[i] > new_adj_path:
                    self.parent_set[i] = node_u
                    self.distance_set[i] = new_adj_path


        # print("temporat set is", self.temporary_set)
        # print("parent set is", self.parent_set)
        print("permanent set is", self.permanent_set)
        print(self.distance_shortest_set)
        # print(self.parent_shortest_set)

    def closeness(self):
        closeness_list = []
        for i in range(self.node_num):
            self.root_code = i
            print(self.root)
            self.algorithm()
            closeness_list.append(sum(self.distance_shortest_set)/(self.node_num-1))
        return closeness_list
