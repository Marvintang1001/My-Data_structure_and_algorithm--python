#! -*- encoding=utf-8 -*-

from computer_principle.doublelinkedlist import DoubleLinkedList, Node


class LRUCache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}  # 保存key和value的映射关系
        self.list = DoubleLinkedList(self.capacity)

    # 每次使用，把使用的节点放到链表最前面，返回值
    def get(self, key):
        if key in self.map:
            node = self.map[key]      # 取出这个key和它的值
            self.list.remove(node)
            self.list.append_front(node)    #把这个缓存放到最前面
            return node.value
        else:
            return -1

    #添加一个缓存
    def put(self, key, value):
        # 先判断key是否已经在缓存里:
        if key in self.map:     #是在缓存里：更新value，放入最前面
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append_front(node)
        else:
            node = Node(key, value)
            #缓存已经满了的话需要先删掉最后一个再往head增加新的：
            if self.list.size >= self.list.capacity-1:
                old_node = self.list.remove()
                self.map.pop(old_node.key)  #删除节点同时要删除本地映射

            self.list.append_front(node)
            self.map[key] = node

    def print(self):
        self.list.print()

# test:
if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2, 2)
    cache.print()
    cache.put(1, 1)
    cache.print()
    cache.put(3, 3)  # 淘汰了（1，1）
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()

