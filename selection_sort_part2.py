# Program Name: selection_sort_part2.py
# Course: CSE2300/Section W02
# Student Name: Joshua Little
# Assignment: Project
# Due Date: 07/23/2023

# Importing modules that will be used in program.
import random
import time

# Getting user input for number of items in array to sort.
n=int(input("Input one number: "))

# Defining arrays.
array1 = []
time_array = []

# Function to sort array using input array.
def selection_sort(array, length):
    
    # Outer for loop to sort array and to create variable equal to array length.
    for i in range(length):
        array_length = i
        # Inner for loop to change array length variable.
        for sort in range(i + 1, length):
            if array[array_length] > array[sort]:
                array_length = sort
         # Switching and sorting.
        (array[i], array[array_length]) = (array[array_length], array[i])

# Creating a length variable equal to the length of the array.
length = n   
             
for i in range(8000):
    array1 = [random.randint(1, 50000) for i in range(n)]
    # Sending Obtaining the time before running the sorting algorithm.
    start_time = time.time()
    # Sending the unsorted array to the sorting function to be sorted.
    selection_sort(array1, length)
    # Obtaining the time after running the sorting algorithm.
    end_time = time.time()
    # Storing the time of a single array being sorted in a variable.
    result = end_time-start_time
    # Storing all times of every array being sorted in an array.
    time_array.append(result)
    
# Calculating total time of sorting algorithm by adding together the time of every individual sort.        
total = sum(time_array)
# Calculating average time of a sort by dividing the total time taken by the number of times the sorting algorithm was ran.
average_time = total/8000

print("Number of items sorted:", n*8000)
print("Average running time for each array:", average_time, "seconds")