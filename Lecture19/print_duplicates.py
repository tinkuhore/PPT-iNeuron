'''
Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. 
Find these repeating numbers in O(n) and using only constant memory space.

Example: 

Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
Output: 1, 3, 6

Explanation: The numbers 1 , 3 and 6 appears more
than once in the array.

Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
Output: 3

Explanation: The number 3 appears more than once
in the array.
'''
from typing import List

def printDuplicates(array: List[int])->None:
    i = 0
    while i < len(array):
        curr = array[i]
        if curr != i:
            if array[curr] != curr and curr !=  -1 and array[curr] != -1:
                array[i], array[curr] = array[curr], array[i]
            elif curr == -1 or array[curr] == -1:
                i += 1
            else:
                print(array[i])
                array[curr] = -1
                i += 1
        else:
            i+=1


array = [1, 2, 3, 6, 3, 6, 1, 3]

printDuplicates(array)