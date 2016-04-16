# 1. list copy ps5 is_valid_word()
a = [1, 2]
b = a # b和a同时指向了[1, 2]，dict也一样
b = a[:] # 不可用于嵌套的list
a = {'a':1}
b = a.copy() # 复制而非引用

# 2. 注意缩进！！！