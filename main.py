import time
from src.dijkstra import DijkstraSPathTree
from src.tarjan import TarjanSPathTree


def main():
    initial_node = int(input("Input node which you want to start with: "))

    while initial_node < 1000:
        initial_choice = input("Input type of data structure (array, heap) you want to use: ")

        if initial_choice == "array":
            start_time = time.time()
            spp_array = DijkstraSPathTree("BallyskateStreet Layout.txt", initial_node)
            spp_array.algorithm()
            end_time = time.time()
            imple_time = end_time - start_time
            print(imple_time)

        elif initial_choice == "heap":
            start_time = time.time()
            spp_heap = TarjanSPathTree("Padgett.txt", initial_node)
            spp_heap.algorithm()
            end_time = time.time()
            # show all detail information
            result_matrix = spp_heap.get_path()
            print(*(i for i in result_matrix), sep="\n")
            """
            show closeness centrality
            """
            # closeness = spp_heap.closeness()
            # print(np.round(closeness, 2))

            imple_time = end_time - start_time
            print(imple_time)

        else:
            print("Please choose 'array' or 'heap': ")

        initial_node = int(input("Input node which you want to start with: "))

    print("The selected node is out of range.")


if __name__ == "__main__":
    main()