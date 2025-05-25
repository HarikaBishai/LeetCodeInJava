# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedInteger:
    def __init__(self, value:None):
        self.integer = None
        self.list = None
        if isinstance(value, int):
            self.integer = value
        else:
            self.list = [NestedInteger(value) for val in value]
    def isInteger(self):
        return self.integer is not None
    def getInteger(self):
        return self.integer
    def getList(self):
        return self.list

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat = []
        self.index = 0
        self._flatten(nestedList)
                
    def _flatten(self, nestedList):
        for val in nestedList:
            if val.isInteger():
                self.flat.append(val.getInteger())
            else:
                self._flatten(val.getList())

    
    def next(self) -> int:
        if self.hasNext():
            val = self.flat[self.index]
            self.index+=1
            return val
        return -1
    def hasNext(self) -> bool:
        return self.index < len(self.flat)

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())