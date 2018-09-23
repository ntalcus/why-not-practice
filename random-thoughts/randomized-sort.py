import numpy as np

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
            print("please initialize with array")
        self.internal_array = A
        self.size = len(A)
        setSamplingSize()
        self.insertionPoints = []
        findInsertPoints()

    def setSamplingSize(self):
        self.sampling_size = (self.size // np.log(size))
        return this.sampling_size


    def findInsertionPoints(self):
        self.sample_size = self.size // self.sampling_size
        for i in range(1, self.sample_size + 1):
            self.insertionPoints.append((A[self.sampling_size * i], self.sampling_size * i))
    
    def insert(self, element):
        for insertPoint in enumerate(self.insertionPoints):
            if element > insertPoint[1][0]:
                self.internal_array.insert(insertPoint[1][1]], element)
                self.size += 1
                return
            else-if element == insertPoint[1]:
                self.internal_array.insert(insertPoint[1][1], element)
                self.insertionPoints[insertPoint[0]] += 1
                self.size += 1
                return
            else:
                pass
        self.internal_array.append(element)
        self.size += 1

    def 