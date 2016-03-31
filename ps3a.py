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

def countSubStringMatchRecursive(target, key):
    if len(target) < len(key):
        return 0
    else:
        i = 0
        i = target.find(key, i) + 1
        
        
        
print(countSubStringMatch('aaaaaaaa', 'aaaaaa'))
print(countSubStringMatchRecursive('aaaaaaaa', 'aaaaaa'))