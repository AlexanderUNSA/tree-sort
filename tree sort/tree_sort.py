import random
import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root

def in_order_traversal(root, sorted_arr):
    if root:
        in_order_traversal(root.left, sorted_arr)
        sorted_arr.append(root.key)
        in_order_traversal(root.right, sorted_arr)

def tree_sort(arr):
    root = None

    for value in arr:
        root = insert(root, value)

    sorted_arr = []
    in_order_traversal(root, sorted_arr)

    return sorted_arr

sizes = [100, 1000, 2000, 3000, 4000, 5000]

for size in sizes:
    # Generate a random list
    lst = [random.randint(0, 1000) for _ in range(size)]

    # Measure the time taken to sort
    start_time = time.time()
    _ = tree_sort(lst)
    elapsed_time = time.time() - start_time

    print(f"Size: {size}, Time: {elapsed_time:.6f} seconds")

