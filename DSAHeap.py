from DSAHeapEntry import DSAHeapEntry

class DSAHeap:
    def __init__(self):
        self.heap = []
        self.count = 0

    def add(self, priority: int, value: object):
        new_entry = DSAHeapEntry(priority, value)
        self.heap.append(new_entry)
        self.count += 1
        self.trickle_up(self.count - 1)

    def remove(self) -> DSAHeapEntry:
        if self.count == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[self.count - 1]
        self.count -= 1
        self.heap.pop()
        self.trickle_down(0)
        return root

    def trickle_up(self, index: int):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].get_priority() > self.heap[parent_index].get_priority():
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def trickle_down(self, index: int):
        while True:
            left_child_idx = (index * 2) + 1
            right_child_idx = (index * 2) + 2
            largest_idx = index

            if left_child_idx < self.count and self.heap[left_child_idx].get_priority() > self.heap[largest_idx].get_priority():
                largest_idx = left_child_idx
            if right_child_idx < self.count and self.heap[right_child_idx].get_priority() > self.heap[largest_idx].get_priority():
                largest_idx = right_child_idx

            if largest_idx == index:
                break
            self.heap[index], self.heap[largest_idx] = self.heap[largest_idx], self.heap[index]
            index = largest_idx

    def heapify(self, array):
        self.heap = array
        self.count = len(array)
        for i in range((self.count // 2) - 1, -1, -1):
            self.trickle_down(i)

def heap_sort(array):
    heap = DSAHeap()
    heap.heapify(array)

    sorted_array = []
    while heap.count > 0:
        sorted_array.append(heap.remove())
    return sorted_array[::-1]

# Main code for testing
if __name__ == "__main__":
    # Test the DSAHeap functionality
    heap = DSAHeap()
    heap.add(5, "Task 1")
    heap.add(3, "Task 2")
    heap.add(8, "Task 3")
    heap.add(1, "Task 4")

    print("Heap contents after adding tasks:")
    for entry in heap.heap:
        print(entry)

    print("\nRemoving highest priority task:")
    removed_task = heap.remove()
    print(removed_task)

    print("\nHeap contents after removal:")
    for entry in heap.heap:
        print(entry)