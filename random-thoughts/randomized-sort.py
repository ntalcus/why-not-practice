from numpy import log
import numpy as np
import sys 
from random import randint
from copy import deepcopy

# Work in progress.
# Algorithms musings by Noah Alcus.

# The goal is to create an array that is probably pretty well sorted.
# When an item is pulled from somewhere in the array, that area is sorted correctly 
# (without changing the rest of the array). Eventually, after the list reaches some
# predetermined amount of unsortedness, the array is resorted correctly with the
# knowledge that each element is approximately where it belongs so that most work can 
# in place more quickly. Something like this probably already exists, this is just as a
# fun personal project to see how I can apply what I'm learning.
# Interested? Reach out.


class SegmentSortedArray:

    def __init__(self, A):
        if not isinstance(A, list):
            print("please initialize with list")
        self.internal_array = deepcopy(A)
        self.internal_array.sort()
        self.size = len(A)
        self.setSamplingSize()
        self.insertion_points = []
        self.findInsertPoints()

    # This function determines how many points should be sampled in the array 
    # to determine approximately where an element should go.
    def setSamplingSize(self):
        self.sampling_size = int (self.size // log(self.size))
        print("Sampling size = " + str(self.sampling_size))
        return self.sampling_size

    # This function uses the sampling_size to find the actual elements of the range and their index.
    # Note that the sample_size is different from the sampling_size. It represents the size of an individual
    # sample.
    # Note that each element of insertion_points is a tuple holding the element at a sample point and the index
    # of that sample point.
    def findInsertPoints(self):
        A = self.internal_array
        self.sample_size = self.size // self.sampling_size
        print("Sample size = " + str(self.sample_size))
        for i in np.arange(0, self.sampling_size ):
            self.insertion_points.append((A[self.sample_size * i], self.sample_size * i))
            print("Element value = " + str(self.insertion_points[-1][0]))
            print("Index value = " + str(self.insertion_points[-1][1]))
            
    
    # This function places an element in approximately the correct location. It does so by placing the
    # element in a location based on the known insertion points.
    def insert(self, element):
        print("beginning insertion")
        for i in np.arange(0, len(self.insertion_points)):
            cInsertPoint = self.insertion_points[i]
            if i + 1 >= len(self.insertion_points):
                nInsertPoint = (sys.maxsize, -1)
            else:
                nInsertPoint = self.insertion_points[i + 1]
            print("low threshold = " + str(cInsertPoint[0]))
            print("high threshold = " + str(nInsertPoint[0]))
            first_comp = element >= cInsertPoint[0] and element <= nInsertPoint[0]
            print("truth value of first comparison: " + str(first_comp))
            sec_comp = element <= cInsertPoint[0]
            print("truth value of second comparison: " + str(sec_comp))
            if element >= cInsertPoint[0] and element <= nInsertPoint[0]:
                self.internal_array.insert(cInsertPoint[1], element)
                self.size += 1
                insertionIndex = i
                break
            elif element <= cInsertPoint[0]:
                self.internal_array.insert(0, element)
                self.size += 1
                insertionIndex = 0
                break
        for i in np.arange(insertionIndex, insertionIndex):
            self.insertion_points[i][1] += 1
        print("ending insertion")            

        # for insertPoint in enumerate(self.insertion_points):

        #     if element > insertPoint[1][0]:
        #         self.internal_array.insert(insertPoint[1][1], element)
        #         self.size += 1
        #         return
        #     else-if element == insertPoint[1]:
        #         self.internal_array.insert(insertPoint[1][1], element)
        #         self.insertion_points[insertPoint[0]] += 1
        #         self.size += 1
        #         return
        #     else:
        #         pass
        # self.internal_array.append(element)
        # self.size += 1
a = []
for i in np.arange(0,15):
    a.append(randint(0, 100))

segArray = SegmentSortedArray(a)

print("The starting array: " + str(segArray.internal_array))
for i in np.arange(0,15):
    rInt = randint(0,100)
    print("Inserting: "+ str(rInt))
    segArray.insert(rInt)
    print("Array after insert: " + str(segArray.internal_array))

print("testing complete")