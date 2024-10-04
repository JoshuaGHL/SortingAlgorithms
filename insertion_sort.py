# Program Name: insertion_sort.py
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
def insertion_sort(arrayinput):
    # Looping from 1 to the length of the array.
    for i in range(1, len(arrayinput)):
        # Create a variable equal to the input number.
        sort = arrayinput[i]
        # Create another variable equal to input number - 1.
        temp = i - 1
        # While loop to sort the array.
        while temp >= 0 and arrayinput[temp] > sort:
            arrayinput[temp + 1] = arrayinput[temp]
            temp -= 1
        # Putting the sorted array in a variable.
        arrayinput[temp + 1] = sort
        
# Sending the unsorted array to the sorting function to be sorted.
insertion_sort(array1)

# Printing the array post-sort
print(array1)