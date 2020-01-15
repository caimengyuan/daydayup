'''
All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab" 


All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz" 

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz" 

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

解答：
    将每一个单项式的符号，数字和字符串分开来，符号和数字结合，对字符串进行排序，使用字典来存储，key为字符串，
对应的value就为对应的符号加数字的值，遍历所以的单项式，如果存在字典中，就改变value值，不存在就直接加入到字典即可。 
最后还需要考虑输出格式的问题。需要按照单项式长度，以及value的大小来按顺序输出。
'''

import re

def simplify(poly):
    terms = {}
    '''

    将输入的多项式按照符号、数字、字母使用正则表达式将他们分割开来，并对他们使用不同的方法进行处理：
        符号：如果符号为‘-’，则将其变为‘-1’，如果为‘+’，则赋值为‘1’
        数字：如果数字存在，则直接同符号相乘，如果不存在则使用1同符号相乘
        字母：对每一组字符串进行排序。这里使用join，是因为排序后的结果是一个列表，而我们需要的是一个字符串。

            构建一个字典terms，将字母作为keys，coef作为values想对应添加到字典中。这里在添加的同时使用了terms.get（）来判断某一个key，
        也就是某一个单项式字母是否已经存在于字典中了。如果存在就将他们相加。不存在则添加该值。
            最后对字典中的元素进行排序。使用两个key来进行排序：第一个是keys的长度从小到大排序，如果长度相同，则使用values进行排序，同样的按照从小到大的方式。
        这一系列操作过后，我们的字典中已经有了计算好的多项式的结果，现在需要将他们链接起来返回简化后的多项式。使用format_term函数来对每一个item进行映射。

            format_term()函数：对字典中的每一个item进行判断，如果item的values为0，则返回‘’也就是空，如果为1，则返回‘+’+ key。如果为-1，则返回‘-’+key，其他情况，
        则返回‘+’+ values + key。将每一个结果使用join链接起来就得到了最后的结果。并且需要移除头尾多出来的‘+’。

    '''
    for sign, coef, vars in re.findall(r'([\-+]?)(\d*)([a-z]*)', poly):
        sign = (-1 if sign == '-' else 1)
        coef = sign * int(coef or 1)
        vars = ''.join(sorted(vars))
        terms[vars] = terms.get(vars, 0) + coef
    # 通过字符串长度和，value大小对字典进行排序。
    terms = sorted(terms.items(), key=lambda item: (len(item[0]), item[0]))
    print(type(terms))
    return ''.join(map(format_term, terms)).strip('+')

def format_term(x):
    if x[1] == 0:
        return ''
    if x[1] == 1:
        return '+' + x[0]
    if x[1] == -1:
        return '-' + x[0]
    return '%+i%s' % (x[1], x[0])


# 测试用例
print(simplify("dc+dcba"))
print(simplify("-abc+3a+2ac"))
print(simplify("a+ca-ab"))