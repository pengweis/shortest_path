from math import ceil


class Heap:
    def __init__(self, arr=None):
        self.heap = []
        self.heap_size = 0
        if arr is not None:
            self.heapify(arr)
            self.heap = arr
            self.heap_size = len(arr)

    def heapify(self, arr):
        """
        Convert a given array into a min heap

        --- Parameters ---
            arr: input array of numbers
        """
        n = len(arr)
        for i in range(int(n / 2), -1, -1):
            self.sift_down(i, arr)

    def sift_up(self, i):
        # Get parent index of the current node
        parent = int(ceil(i / 2 - 1))

        # Check if the parent value is smaller than the newly inserted value
        # if so, then replace the value with the parent value and check with the new parent
        while parent >= 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = int(ceil(i / 2 - 1))

    def sift_down(self, i, arr):
        """
        Assuming sub trees are already min heaps, converts tree rooted at current indx into a min heap.
        :param indx: Index to check for min heap
        """
        # Get index of left and right child of indx node
        left_child = i * 2 + 1
        right_child = i * 2 + 2

        smallest = i

        # check what is the smallest value node in indx, left child and right child
        if left_child < len(arr):
            if arr[left_child] < arr[smallest]:
                smallest = left_child
        if right_child < len(arr):
            if arr[right_child] < arr[smallest]:
                smallest = right_child

        # if indx node is not the smallest value, swap with the smallest child
        # and recursively call min_heapify on the respective child swapped with
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.sift_down(smallest, arr)

    def insert(self, value):
        """
        Inserts an element in the min heap
        :param value: value to be inserted in the heap
        """
        self.heap.append(value)
        self.sift_up(self.heap_size)
        self.heap_size += 1

    def delete(self, indx):
        """
        Deletes the value on the specified index node
        :param indx: index whose node is to be removed
        :return: Value of the node deleted from the heap
        """
        if self.heap_size == 0:
            print("Heap Underflow!!")
            return

        self.heap[-1], self.heap[indx] = self.heap[indx], self.heap[-1]
        self.heap_size -= 1

        self.sift_down(indx, self.heap)

        return self.heap.pop()

    def delete_min(self):
        """
        Extracts the minimum value from the heap
        :return: extracted min value
        """
        return self.delete(0)

    def print(self):
        print(*self.heap)


heap = Heap([1, 3, 9, 7, 5])
heap.print()

heap.insert(5)
heap.print()
