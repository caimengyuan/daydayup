'''
    区别浅拷贝和深拷贝：
        浅拷贝是新建了一个跟原对象一样的类型，但其内容是对原对象内容的引用

        list tuple默认都是浅拷贝

        原字典与赋值、浅拷贝之间紧密相连，一方改变，对方随之改变！
        原字典与深拷贝，深拷贝独立门户，从此与原字典无关！
'''

def deepcopy(data):
    # 新创建的列表
    listdata = []
    if len(data) != 1:
        for i in data:
            # 如果i是data类型的，则调用字典处理函数copydict()
            if isinstance(i, dict):
                dictdata = copydict(i)
                listdata.append(dictdata)
            # 如果是元组和列表则递归调用deepcopy函数
            elif isinstance(i, list) or isinstance(i, tuple):
                listdata1 = deepcopy(i)
                listdata.append(listdata1)
            # 其他不可变类型的数据就添加到listdata中
            else:
                listdata.append(i)
    else:
        return data
    return listdata

# 字典类型的处理函数
def copydict(data):
    dict1 = {}
    # 遍历字典
    for keys, values in data.items():
        if isinstance(values, dict):
            numdict = copydict(values)
            dict1[keys] = numdict
        else:
            value = deepcopy(values)
            dict1[keys] = value
    return dict1

if __name__ == '__main__':
    numlist = [[1, 2, [3, 4, 5]], 34, "number",
               {"name": {"fistname": "孙", "lastName": "悟空","listname":[1,2,3]}}]