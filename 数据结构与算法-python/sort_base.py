# -*- coding: utf-8 -*-
from random import randint
import timeit


def bubbleSort(alist):
    # exchange = False  # 这里写错了
    for i in range(len(alist) - 1, 0, -1):      # 降序
        exchange = False    # 假如未到最后一次就碰巧全排齐了
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                exchange = True
        if not exchange:
            break
    return alist


def selectionSort(alist):
    for i in range(len(alist)):
        minposition = i
        for j in range(i, len(alist)):
            if alist[minposition] > alist[j]:
                minposition = j
        alist[i], alist[minposition] = alist[minposition], alist[i]
    return alist


def insertionSort(alist):
    for i in range(1, len(alist)):
        currentvalue = alist[i]
        position = i
        while alist[position - 1] > currentvalue and position > 0:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentvalue
    return alist


def shellSort(alist):
    gap = len(alist) // 2   # 地板除
    while gap > 0:
        for startpos in range(gap):
            gapInsertionSort(alist, startpos, gap)
        gap = gap // 2
    return alist


def gapInsertionSort(alist, startpos, gap):
    # 希尔排序的辅助函数，其实就是插入排序，但是多了个gap步长进行分组后的插入排序
    for i in range(startpos + gap, len(alist), gap):
        position = i
        currentvalue = alist[i]     #copy
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


max = 50
list = [randint(0, max) for x in range(max)]  # 一共5000个数，数值范围是【-5000，5000】
# 使用切片可以真正将一份list复制给其他变量，如果不用切片，即alist=list，只是指针而已。
alist = list[:]
blist = list[:]
clist = list[:]
dlist = list[:]

'''
运行次数(number)只能设置成1，因为内存中alist、blist等指向同一个对象，该对象第一次排序后就已经是有序列表了。
所以在这种情况下会发生有趣的现象。按照短路冒泡排序的性质，它在碰到一个有序列表以后会立刻停止遍历，所以不管它的number是1还是10，time都几乎没变化
但其他排序方法，就算对有序列表进行排序，交换是不需要了，但是还要遍历&比较，所以他们的运行次数变多的话，time依旧变大
之前我就是把number设置成100，发现短路冒泡排序简直太快了，才发现这个问题。
'''
t1 = timeit.Timer('bubbleSort(alist)', 'from __main__ import bubbleSort,alist')
a = bubbleSort(alist)
print('短路冒泡排序: %s s' % t1.timeit(number=1))
print(a)

# t2 = timeit.Timer('selectionSort(blist)', 'from __main__ import selectionSort,blist')
# print('选择排序: %s s' % t2.timeit(number=1))
#
# t3 = timeit.Timer('insertionSort(clist)', 'from __main__ import insertionSort,clist')
# print('插入排序: %s s' % t3.timeit(number=1))
#
# t4 = timeit.Timer('shellSort(dlist)', 'from __main__ import shellSort,dlist')
# print('希尔排序: %s s' % t4.timeit(number=1))
