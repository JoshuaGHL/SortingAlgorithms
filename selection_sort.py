# Program Name: selection_sort.py
# Course: CSE2300/Section W02
# Student Name: Joshua Little
# Assignment: Project
# Due Date: 07/23/2023

# Importing modules that will be used in program.
import random

# Getting user input for numbers.
num=int(input("Number: "))

# Defining arrays.
array1 = []

# Populating array with the user inputted number of random numbers from 1-50000.
array1 = [random.randint(1, 50000) for i in range(num)]

# Printing the array pre-sort.
print(array1)

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
length = len(array1)
# Sending the unsorted array as well as the length of the array to the sorting function to be sorted.
selection_sort(array1, length)

# Printing the array post-sort
print(array1)