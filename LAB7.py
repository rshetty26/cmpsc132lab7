
# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

class MaxBinaryHeap:
    '''
        >>> h = MaxBinaryHeap()
        >>> h.getMax
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [10, 5]
        >>> h.insert(14)
        >>> h._heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(14)
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> h.insert(20)
        >>> h
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.insert(20)
        >>> h
        [20, 20, 14, 14, 2, 10, 11, 5, 9]
        >>> h.getMax
        20
        >>> h._leftChild(1)
        20
        >>> h._rightChild(1)
        14
        >>> h._parent(1)
        >>> h._parent(6)
        14
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMax()
        20
        >>> h._heap
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.deleteMax()
        20
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> len(h)
        7
        >>> h.getMax
        14
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMax(self):
        # YOUR CODE STARTS HERE
        if not len(self._heap) == 0:
            return self._heap[0]
        return None
        pass
    
    def _parent(self,index):
        # YOUR CODE STARTS HERE
        x = index//2
        return self._heap[x-1]
        pass
        

    def _leftChild(self,index):
        # YOUR CODE STARTS HERE
        x = index*2
        if not len(self._heap) < x:
            return self._heap[x-1]
        return None
        pass


    def _rightChild(self,index):
        # YOUR CODE STARTS HERE
        x = index*2 +1
        if not len(self._heap) < x:
            return self._heap[x-1]
        return None
        pass
         

    def insert(self,x):
        # YOUR CODE STARTS HERE
        self._heap.append(x)
        index = len(self._heap)-1
        while not index == 0 and self._parent(index+1) < self._heap[index]:
            parentindex = ((index+1)//2)-1
            self._heap[parentindex], self._heap[index] = self._heap[index], self._heap[parentindex]
            index = parentindex
        pass

    def deleteMax(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            removed=self._heap[0]
            self._heap=[]
            return removed 

        # YOUR CODE STARTS HERE
        removed = self._heap[0]
        self._heap[0] = self._heap[len(self._heap)-1]
        self._heap = self._heap[:-1]

        index = 0
        while (self._leftChild(index + 1)) and (self._rightChild(index + 1)) and (self._leftChild(index + 1) > self._heap[index] or self._rightChild(index + 1) > self._heap[index]) and (index < len(self._heap)):
            if self._leftChild(index + 1) >= self._rightChild(index + 1):
                childindex = ((index+1)*2)-1
            else:
                childindex = ((index+1)*2)
            self._heap[childindex], self._heap[index] = self._heap[index], self._heap[childindex]
            index = childindex
        if self._leftChild(index + 1):
            if self._leftChild(index + 1) > self._heap[index]:
                childindex = ((index+1)*2)-1
                self._heap[childindex], self._heap[index] = self._heap[index], self._heap[childindex]
        return removed
        pass


def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [8, 5, 4, 3.1, 2, 1, 0, -15, -15, -15]
    '''
    # YOUR CODE STARTS HERE
    x = MaxBinaryHeap()
    final = []
    for y in numList:
        x.insert(y)
    while len(x) > 0:
        final.append(x.deleteMax())
    return final
    pass


if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(heapSort, globals(), name='LAB7',verbose=False)




