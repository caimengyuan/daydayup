'''
The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears

字符串融合，编写一个函数，给定三个参数，s,part1,part2
判断s是不是有part1和part2组合而成的，并且part1和part2的字母顺序应该和S里的字母顺序一致。
函数嵌套可以解决这个问题

'''
# import re

def is_merge(s, part1, part2):
    if s == part1 + part2:
        return True
    if len(part1)+len(part2) != len(s) or sorted(list(s)) != sorted(list(part1+part2)):
        return False
    list1 = []
    list2 = []
    for a in part1:
        if a.isalnum():
            list1.append(a)
        else:
            a = '\\' + a
            list1.append(a)
    for b in part2:
        if b.isalnum():
            list2.append(b)
        else:
            b = '\\' + b
            list2.append(b)
    getRegex1 = re.compile('.*'+'.*'.join(list1)+'.*')
    getRegex2 = re.compile('.*'+'.*'.join(list2)+'.*')
    return True if getRegex1.match(s) and getRegex2.match(s) else False

# 递归实现
def is_merge(s, part1, part2):
    if not part1:
      return s == part2
    if not part2:
      return s == part1
    if not s:
      return part1 + part2 == ''
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
      return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
      return True
    return False




# 主要是相对位置的判断是否一致
def is_merge_wrong(s, part1, part2):
    if len(s) != (len(part1) + len(part2)):
        return False

    # where are the characters in the desired string?
    part1_pos = [s.find(x) for x in part1]
    part2_pos = [s.find(x) for x in part2]

    # are they in order? i.e. does the position keep increasing? 
    part1_increases = [x < y for x,y in zip(part1_pos,part1_pos[1:])]
    part2_increases = [x < y for x,y in zip(part2_pos,part2_pos[1:])]

    # these prints will show you what is going on ...
    print(part1_pos,part1_increases)
    print(part2_pos,part2_increases)


    if all(part1_increases) and all(part2_increases):
         for i in part1:
            s = re.sub(i, '', s, 1)
        if s == part2:
            return True
        return False

    return False