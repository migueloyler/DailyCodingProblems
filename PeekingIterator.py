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
        self.iterator = iterator
        self.index = 0
        #print(self.iterator.__dict__) -> here we see that in the Iterator object, the nums array is            initialized as "self.v = nums", not exactly sure why they did this...
        
        #print(self.iterator.v)
        #^^^ so for some reason LeetCode initializes the nums list of the iterator to "self.v = nums"
        #instead of "self.nums = nums", so in order to access the nums array, I call self.v
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        #print(self.index)
        if self.hasNext():
            return self.iterator.v[self.index]
        

    def next(self):
        """
        :rtype: int
        """
        #print(self.index)
        if self.hasNext():
            item = self.iterator.v[self.index]
            self.index += 1
            return item
        

    def hasNext(self):
        """
        :rtype: bool
        """
        #print(self.index)
        if self.index == len(self.iterator.v):
            return False
        return True
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
