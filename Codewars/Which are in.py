'''
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]
'''

def in_array(array1, array2):
    # your code
    print(array1, array2)
    res = []
    for i in array2:
        for j in array1:
            if i.find(j) >= 0:
                res.append(j)
    res = list(set(res))
    return sorted(res, key=len) 


def in_array(array1, array2):
    # your code
    l=[]
    for i in array1:
        for j in array2:
            if i in j:   # and not i in l:
                l.append(i)
                break  #注意什么时候可以不写
    l=list(set(l))#set[]会变成{}，sort只用于[],所以还要在list()一样 #sorted()就可以作用于{}！！
    l.sort()#排序
    return l



def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})
    
in_array(['cod', 'code', 'wars', 'ewar'],['lively', 'alive', 'harp', 'sharp', 'armstrong', 'codewars'])