#! -*- encoding=utf-8 -*-

from computer_principle.doublelinkedlist import DoubleLinkedList, Node

class LFUNode(Node):
    def __init__(self, key, value):
        self.freq = 0   # 新增一个mode属性
        super(LFUNode, self).__init__(key, value)   # 这是python2的写法。python3：super().__init__(key, value)


class LFUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}  # 保存key和value的映射关系
        # key: 频率， value：频率对应的双向链表
        self.freq_map = {}
        self.list = DoubleLinkedList(self.capacity)
        self.size = 0

    # 更新节点频率的操作
    def __update_freq(self, node):
        freq = node.freq    # 这个节点之前所在的频率的双向链表

        # 删除:
        node = self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]

        # 更新:
        freq = freq+1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()
        self.freq_map[freq].append(node)


    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.__update_freq(node)
        return node.value


    def put(self, key, value):
        if self.capacity == 0:
            return

        # 缓存命中：
        if key in self.map:
            node = self.map.get(key)
            node.value = value
            self.__update_freq(node)

        # 缓存没有命中：
        else:
            # 判读缓存是否满了：
            if self.capacity == self.size:
                # 满了就淘汰频率最低，最早进去的那个缓存：
                min_freq = min(self.freq_map)       #freq_map里的key都是数字
                node = self.freq_map[min_freq].pop()    #默认pop是head
                del self.map[node.key]
                self.size -= 1
            # 下面是不管是否命中都会执行的步骤:
            node = LFUNode(key, value)
            node.freq = 1
            self.map[key] = node
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleLinkedList()
            node = self.freq_map[node.freq].append(node)
            self.size += 1

    # 打印所有频率链表：
    def print(self):
        print('****************************')
        for k, v in self.freq_map.items():      # 字典的items方法：返回可遍历的(键, 值) 元组数组
            print('Freq = {}'.format(k))
            self.freq_map[k].print()
        print('****************************')
        print()

# test:
if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()
    print(cache.get(1))
    cache.print()
    cache.put(3, 3)     #会造成{2,2}的淘汰
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()
    cache.put(4, 4)
    cache.print()
    print(cache.get(1))
    cache.print()
    # print(cache.get(2))
    print(cache.get(3))
    cache.print()
    print(cache.get(4))
    cache.print()


