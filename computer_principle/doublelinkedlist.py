#! -*- encoding=utf-8 -*-

#prve和next是迭代器的方法

# 链表节点：
class Node:
    def __init__(self, key, value):
        self.key = key      #键
        self.value = value      #值
        self.prev = None
        self.next = None

    def __str__(self):  # print实例时打印出来的内容，不定义可以调用，重新定义后则可以定制打印内容
        val = '{%d: %d}' % (self.key, self.value)
        return val

    def __repr__(self):  # 直接输出实例名打印出来的内容，不定义可以调用，重新定义后则可以定制打印内容
        val = '{%d: %d}' % (self.key, self.value)
        return val


class DoubleLinkedList:
    def __init__(self, capacity=0xffff):  # capacity是容量值，默认最大
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0  # 以上都是默认

    # 从头部添加：
    def __add_head(self, node):
        if not self.head:  # 没有节点
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.prev = None
        else:
            node.next = self.head  # 新节点的next指向现在的head
            self.head.prev = node  # 把head的前向指针指向新节点
            self.head = node  # 把head指向新节点
            self.head.prev = None  # 把head的前向指针指向空
            self.size += 1
            return node

    # 从尾部添加节点:
    def __add_tail(self, node):
        if not self.tail:
            self.tail = node
            self.head = node
            self.tail.next = None
            self.tail.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node

    #从尾部删除(弹出尾部节点)
    def __del_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    # 从头部删除（弹出头部节点）
    def __del_head(self):
        if not self.head:   #没有头部节点
            return
        node = self.head    #取出头部节点
        if node.next:   #如果头部节点有下一个节点
            self.head = node.next
            self.head.prev = None
        else:   #如果头部节点没有下一个节点
            self.tail = self.head = None
        self.size -= 1
        return node

    # 任意节点删除：
    def __remove(self, node):
        # 如果node=None，默认删除尾部节点
        if not node:
            node = self.tail
        if node == self.tail:
            self.__del_tail()
        elif node == self.head:
            self.__del_head()
        else:
            node.prev.next = node.next  #被删除节点的上一个节点的next指针指向被删除节点的下一个节点
            node.next.prev = node.prev
            self.size -= 1
        return node


    #对外实现的api：

    #弹出头部节点：
    def pop(self):
        return  self.__del_head()

    #往尾部添加节点：
    def append(self, node):
        return self.__add_tail(node)

    #往头部添加节点：
    def append_front(self, node):
        return self.__add_head(node)

    #删除节点：
    def remove(self, node=None):    #默认为空
        return self.__remove(node)

    #打印当前链表
    def print(self):
        p = self.head
        line = ''   #存储链表的字符串
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += '=>'
        print(line)


#简单测试：#
if __name__ == '__main__':
    l = DoubleLinkedList(10)
    nodes = []
    for i in range(10):
        node = Node(i, i)
        nodes.append(node)      #往nodes列表的尾部增加

    l.append(nodes[0])
    l.print()
    l.append(nodes[1])
    l.print()
    l.pop()     #弹出头部节点
    l.print()
    l.append(nodes[2])  #尾部增加一个节点
    l.print()
    l.append_front(nodes[3])    #头部增加一个节点
    l.print()
    l.append(nodes[4])
    l.print()
    l.remove(nodes[2])  #删除节点2
    l.print()
    l.remove()  #默认删除尾部节点
    l.print()
