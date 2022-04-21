class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict1 = []
        

    def add(self, key: int) -> None:
        if self.dict1 is []:
            self.dict1.append(key)
        else:
            if key in self.dict1:
                pass
            else:
                self.dict1.append(key)

    def remove(self, key: int) -> None:
        if key in self.dict1:
            self.dict1.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.dict1:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)