from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity=10):
        self.od =OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)     # 升序，第一个是最少使用那个

# test:
cache = LRUCache()
k = 10
for i in range(k):
    cache.od[i] = i
print(cache.od.keys())
print('key = 5, value =', cache.get(5))
print(cache.od.keys())
cache.put(6, 'happy')
print(cache.od)
cache.put(20, 'xixi')
print(cache.od)

