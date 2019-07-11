# python函数传参的问题：
# def clear_list(l):
#     l = []
#
# def fl(l=[1]):
#     l.append(1)
#     print(l)

# ll = [1, 2, 3]
# clear_list(ll)
# print(ll)
#
# fl()
# fl()

########################################
# python **kwrgs问题：

# def print_kwargs(**kwargs):
#     print(type(kwargs), kwargs)
#     for k, v in kwargs.items():
#         print('{} : {}'.format(k,v))
#
# print_kwargs(**dict(a=1, b=2))

#########################################
# python 字典深拷贝浅拷贝问题：
import copy

dict1 = {'name':'jack', 'num':[1, 2, 3]}
dict2 = dict1   # 证明字典是可变对象
dict3 = dict1.copy()
dict4 = copy.deepcopy(dict1)

# test:
# dict1['name'] = 'Marvin'
# dict2['num'].remove(1)
print('dict1 = ', dict1)
print('dict2 = ', dict2)
print('dict3 = ', dict3)
print('dict4 = ', dict4)
print('')

# test2：
dict3['num'] = [6, 6, 6]
print('dict1 = ',dict1)
print('dict3 = ',dict3)
print('')

dict3 = dict1.copy()
dict3['num'].append(7)
print('dict1 = ',dict1)
print('dict3 = ',dict3)

# test3：
# print('')
# print('test2----------------')
# dict1['num'] = [6, 6, 6]
# print('dict1 = ', dict1)
# print('dict2 = ', dict2)
# print('dict3 = ', dict3)
