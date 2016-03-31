from string import *

def countSubStringMatch(target, key):
    i = 0
    count = 0
    if len(target) >= len(key):
        while i+len(key) <= len(target):
            i = target.find(key, i) + 1
            if i != 0:
                count += 1
    return count

# ???Recursive
def countSubStringMatchRecursive(target, key):
    i = []
    if len(target) < len(key):
        return 0
    elif target.find(key) != -1:
        i.append(target.find(key))
    countSubStringMatchRecursive(target[i[-1]+1: len(target)], key)
    return len(i)
        
        
        
print(countSubStringMatch('aaaaaaaa', 'aaaaaa'))
print(countSubStringMatchRecursive('aa', 'a'))