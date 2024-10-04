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

# Function to perform Quicksort.
def quicksort(arrayinput):
    # Base case: an array with 0 or 1 element is already sorted.
    if len(arrayinput) <= 1:
        return arrayinput
    else:
        # Select the pivot (can use various methods, here we choose the last element).
        pivot = arrayinput[len(arrayinput) - 1]
        left = [x for x in arrayinput[:-1] if x <= pivot]
        right = [x for x in arrayinput[:-1] if x > pivot]

        # Recursively sort elements smaller and larger than pivot and concatenate.
        return quicksort(left) + [pivot] + quicksort(right)

# Running the sorting algorithm 8000 times for accurate timing results.
for i in range(8000):
    # Creating an array of random integers between 1 and 50000 based on user input number.
    array1 = [random.randint(1, 50000) for i in range(n)]
    # Obtaining the time before running the sorting algorithm.
    start_time = time.time()
    # Sending the unsorted array to the sorting algorithm to be sorted.
    sorted_array = quicksort(array1)
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