# Importing modules that will be used in the program.
import random
import time

# Getting user input for numbers.
n = int(input("Input one number: "))
# Initiating running_time to 0.
running_time = 0

# Defining arrays.
array1 = []
dict_arrays = {}
time_array = []

# Class representing a Node in the Binary Search Tree.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to insert a new node in the BST.
def insert(root, key):
    # If the tree is empty, return a new node.
    if root is None:
        return Node(key)
    # Otherwise, recur down the tree.
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Function for in-order traversal of the tree, which returns sorted elements.
def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
        
# Function to perform Tree Sort.
def tree_sort(arrayinput):
    if not arrayinput:
        return []

    # Build the binary search tree.
    root = Node(arrayinput[0])
    for i in range(1, len(arrayinput)):
        insert(root, arrayinput[i])

    # Perform in-order traversal to get the sorted array.
    sorted_array = []
    inorder_traversal(root, sorted_array)
    return sorted_array

# Running the sorting algorithm 8000 times for accurate timing results.
for i in range(8000):
    # Creating an array of random integers between 1 and 50000 based on user input number.
    array1 = [random.randint(1, 50000) for i in range(n)]
    # Obtaining the time before running the sorting algorithm.
    start_time = time.time()
    # Sending the unsorted array to the sorting algorithm to be sorted.
    sorted_array = tree_sort(array1)
    # Obtaining the time after running the sorting algorithm.
    end_time = time.time()
    # Storing the time of a single array being sorted in a variable.
    result = end_time - start_time
    # Storing all times of every array being sorted in an array.
    time_array.append(result)

# Calculating total time of sorting algorithm by adding together the time of every individual sort.        
total = sum(time_array)
# Calculating average time of a sort by dividing the total time taken by the number of times the sorting algorithm was ran.
average_time = total / 8000

# Displaying results.
print("Number of items sorted:", n * 8000)
print("Average running time for each array:", average_time, "seconds")