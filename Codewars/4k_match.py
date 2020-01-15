
'''
d, _ = 0.5, None

crosstable([
    'Emmett Frost', 'Cruz Sullivan', 'Deandre Bullock', 'George Bautista', 'Norah Underwood', 'Renee Preston'], [
    [_, 1, 0, 0, d, 0],
    [0, _, d, 1, 0, 0],
    [1, d, _, d, d, d],
    [1, 0, d, _, d, d],
    [d, 1, d, d, _, d],
    [1, 1, d, d, d, _]])

# returns
#  Player           1 2 3 4 5 6  Pts   SB
==========================================
1  Renee Preston      = = = 1 1  3.5  7.25
2  Deandre Bullock  =   = = = 1  3.0  6.75
   Norah Underwood  = =   = 1 =  3.0  6.75
4  George Bautista  = = =   0 1  2.5  6.25
5  Cruz Sullivan    0 = 0 1   0  1.5  4.00
6  Emmett Frost     0 0 = 0 1    1.5  3.00

'''

import copy

def crosstable(players, result):
#     return (
#         "#  Player             1 2 3  Pts  SB\n"
#         "=====================================\n"
#         "1  Boris Spassky        1 =  1.5 1.25\n"
#         "2  Garry Kasparov     0   1  1.0 0.50\n"
#         "3  Viswanathan Anand  = 0    0.5 0.75")
    num_players = len(players)
    str_num = [str(i) for i in range(num_players+1)]
    str_num = ' '.join(str_num[1:])
    res = f'# Player {str_num} Pts SB\n'
    res += '==================================================\n'
    print(res)
    dict_res = {}
    for i in range(len(result)):
        sum_n = sum([0 if x==None else x for x in result[i]])
        result[i].append(sum_n)
        
    results = copy.deepcopy(result)
    for i in range(len(result)):
        SB_num1, SB_num2 = 0, 0
        for j in range(len(result[0])):
            if result[i][j] == 1:
                SB_num1 += result[j][-1]
            if result[i][j] == 0.5:
                SB_num2 += result[j][-1]

        results[i].append(SB_num1 + SB_num2 / 2)

    # 获取列表的下标和值
    results = sorted(enumerate(results), key=lambda x:x[1][num_players:], reverse=True)
    flag = [i[0] for i in results]

    for i in range(len(results)):
        reslist = [None] * (num_players+2)
        for j in range(len(reslist)):
            if j >= num_players:
                reslist[j] = results[i][1][j]
            else:    
                reslist[j] = results[i][1][flag[j]]
        results[i] = reslist

    for i in range(num_players):
        dict_res[players[flag[i]]] = results[i]
    for keys, values in dict_res.items():
        for i in range(len(values)):
            if values[i] == None:
                values[i] = ' '
            if values[i] == 0.5:
                values[i] = '='
            else:
                values[i] = str(values[i])
        res = str(keys) + ' '.join(values)
        print(res)

_, d = None, 0.5
crosstable(["Emmett Frost", "Cruz Sullivan", "Deandre Bullock", "George Bautista", "Norah Underwood", "Renee Preston"], 
    [[_, 1, 0, 0, d, 0],
    [0, _, d, 1, 0, 0],
    [1, d, _, d, d, d],
    [1, 0, d, _, d, d],
    [d, 1, d, d, _, d],
    [1, 1, d, d, d, _]])
# expected = "#  Player           1 2 3 4 5 6  Pts   SB\n"
#     "==========================================\n"
#     "1  Renee Preston      = = = 1 1  3.5  7.25\n"
#     "2  Deandre Bullock  =   = = = 1  3.0  6.75\n"
#     "   Norah Underwood  = =   = 1 =  3.0  6.75\n"
#     "4  George Bautista  = = =   0 1  2.5  6.25\n"
#     "5  Cruz Sullivan    0 = 0 1   0  1.5  4.00\n"
#     "6  Emmett Frost     0 0 = 0 1    1.5  3.00"
# print(type(expcted))