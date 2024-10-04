# Importing necessary modules for time and random number generation
import random
import time

# Getting user input for number of elements to be sorted.
n = int(input("Input one number: "))
# Initiating running_time to 0.
running_time = 0

# Defining arrays.
array1 = []
dict_arrays = {}
time_array = []

# Function to implement merge sort algorithm.
def merge_sort(arrayinput):
    # If the array has more than 1 element, split it into two halves.
    if len(arrayinput) > 1:
        # Finding the middle of the array.
        mid = len(arrayinput) // 2
        # Dividing the array elements into two halves.
        left_half = arrayinput[:mid]
        right_half = arrayinput[mid:]
        
        # Recursively sorting both halves.
        merge_sort(left_half)
        merge_sort(right_half)

        # Variables for keeping track of merging process.
        i = j = k = 0

        # Merging the sorted halves.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arrayinput[k] = left_half[i]
                i += 1
            else:
                arrayinput[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in the left half.
        while i < len(left_half):
            arrayinput[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in the right half.
        while j < len(right_half):
            arrayinput[k] = right_half[j]
            j += 1
            k += 1

# Running the sorting algorithm 8000 times for accurate timing results.
for i in range(8000):
    # Creating an array of random integers between 1 and 50000 based on user input number.
    array1 = [random.randint(1, 50000) for i in range(n)]
    # Obtaining the time before running the sorting algorithm.
    start_time = time.time()
    # Sending the unsorted array to the sorting algorithm to be sorted.
    merge_sort(array1)
    # Obtaining the time after running the sorting algorithm.
    end_time = time.time()
    # Storing the time of a single array being sorted in a variable.
    result = end_time - start_time
    # Storing all times of every array being sorted in an array.
    time_array.append(result)

# Calculating total time of sorting algorithm by adding together the time of every individual sort.        
total = sum(time_array)
# Calculating average time of a sort by dividing the total time taken by the number of times the sorting algorithm was run.
average_time = total / 8000

# Displaying results.
print("Number of items sorted:", n * 8000)
print("Average running time for each array:", average_time, "seconds")