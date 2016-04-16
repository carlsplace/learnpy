# 1. list copy ps5 is_valid_word()
a = [1, 2]
b = a # b和a同时指向了[1, 2]，dict也一样
b = a[:] # 不可用于嵌套的list
a = {'a':1}
b = a.copy() # 复制而非引用

# 2. 注意缩进！！！

# 3. 熟悉内置函数功能！ps5_ghost.py写不出来，是因为忘了find()函数 ---> 阅读《Python核心编程》的必要性