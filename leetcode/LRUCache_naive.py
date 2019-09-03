# Naive Implementation

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = {}
        self.indexes = []
        

    def get(self, key: int) -> int:
        
        if not key in self.indexes: return -1
        self.indexes.sort(key = key.__eq__)
        return self.stack[key]
        

    def put(self, key: int, value: int) -> None:
        keys = self.indexes
        if not key in keys:
            if len(keys) == self.capacity:
                # find the last element in index array
                # remove element
                k = keys.pop(0)
                self.stack.pop(k)
            # append on top of array
            keys.append(key)
        keys.sort(key = key.__eq__)
        self.stack[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)