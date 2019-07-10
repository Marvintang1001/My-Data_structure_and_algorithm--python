# -*- coding: utf-8 -*-
import re
from repo import BinarySearchTree
import timeit

# 词频统计出现在课程5-4的最后，老师想检测二分搜索树的查找效率并与顺序数组作比较。这里我就不比较了，只实现这个功能。
# 其实词频统计直接用python的Counter对象就行了。

tree = BinarySearchTree()
with open('bible.txt', 'r', encoding='utf-8') as f:
    file = f.read()
words = list(re.split('\W+', file))


def countWord():
    for word in words:
        word = word.lower()
        if tree[word] is None:  # {key : value} ==> {word : num}
            tree[word] = 1  # word第一次出现，value把None改成1
        else:
            tree[word] = tree[word] + 1     # 可以写的这么简洁，归功于魔法方法：__getitems__
    print(tree['god'])      # 二叉搜索树的工作是找出这个value


t2 = timeit.Timer('countWord()', 'from __main__ import countWord ')
print('耗时: %s s' % t2.timeit(number=1))
