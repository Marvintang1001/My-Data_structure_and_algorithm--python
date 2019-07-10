#! -*- encoding=utf-8 -*-

from computer_principle.doublelinkedlist import DoubleLinkedList, Node


class FIFOCache(object):
    def __init__(self, capacity):
        self.capacity = capacity  # 容量大小
        self.size = 0
        self.map = {}  # 保存key和value的映射关系
        self.list = DoubleLinkedList(self.capacity)

    # 从缓存中获取key对应的value内容，如果key不存在就返回-1
    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map.get(key)  # get是dict的方法，取出key对应的value
            return node.value

    # 添加一个缓存
    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.map:  # 如果key已经存在，就把它的先删掉掉再放新的到最后
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value  # 覆盖
            self.list.append(node)
        else:
            if self.size == self.capacity:  # 如果该key是新的，先判断缓存是否满了，满了要pop头部节点
                node = self.list.pop()
                del self.map[node.key]  # 本地映射map中删除这个head节点
                self.size -= 1
            node = Node(key, value)  # 新增一个节点
            self.list.append(node)
            self.map[key] = node  # 本地map中增加这个节点的映射
            self.size += 1

    def print(self):
        self.list.print()


# test:
if __name__ == '__main__':
    cache = FIFOCache(2)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()
    print(cache.get(1))
    cache.put(3, 3)     # 淘汰了（1，1）
    cache.print()
    print(cache.get(2))
    cache.print()
    cache.put(4, 4)
    cache.print()
    print(cache.get(1))
