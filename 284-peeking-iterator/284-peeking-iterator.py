# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.arr = iterator
        self.a = [self.arr.next()]
        self.pointer = 0
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.a[self.pointer]
        

    def next(self):
        """
        :rtype: int
        """
        self.pointer += 1
        val = self.arr.next()
        if(val > -100000):
            self.a.append(val)
        
        
        
        return self.a[self.pointer-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        print(self.pointer , self.a)
        return self.pointer < len(self.a)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].