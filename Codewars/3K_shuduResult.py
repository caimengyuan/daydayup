# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python

class Solution():
    def __init__(self, sudo_ku_data):
        if not isinstance(sudo_ku_data, list):
            raise TypeError(f'sudo_ku_data params must a list, but {sudo_ku_data} is a {type(sudo_ku_data)}')
        
        if len(sudo_ku_data) != 9 or len(sudo_ku_data[0]) != 9:
            raise TypeError(f'sudo_ku_data params must a 9*9 list, but {sudo_ku_data} is a {len(sudo_ku_data)}*{len(sudo_ku_data[0])} list')
        
        self.sudo_ku = sudo_ku_data

        # 存放每一行已有的数据
        self.every_row_data = {}
        # 每一列已有的数字
        self.every_column_data = {}
        # 每一个3*3宫内有的数字
        self.every_three_to_three_data = {}
        # 每一个空缺的位置
        self.vacant_position = []
        # 每一个空缺位置尝试了的数字
        self.every_vacant_position_tried_values = {}

    # 编写添加每一行、每一列、每一宫方法
    def _add_row_data(self, row, value):
        if row not in self.every_row_data:
            self.every_row_data[row] = set()
        
        if value in self.every_row_data[row]:
            raise TypeError(f'params {self.sudo_ku} is a valid Sudoku')
        
        self.every_row_data[row].add(value)
    
    def _add_column_data(self, column, value):
        if column not in self.every_column_data:
            self.every_column_data[column] = set()
        
        if value in self.every_column_data[column]:
            raise TypeError(f'params {self.sudo_ku} is a valid Sudoku')
        
        self.every_column_data[column].add(value)
    
    def _add_three_to_three_data(self, row, column, value):
        key = self._get_three_to_three_key(row, column)

        if key not in self.every_three_to_three_data[key]:
            self.every_three_to_three_data[key] = set()
        
        if value in self.every_three_to_three_data[key]:
            raise TypeError(f'params {self.sudo_ku} is a invalid SudoKu')
        
        self.every_three_to_three_data[key].add(value)
    
    def _get_three_to_three_key(self, row, column):
        if row in [0, 1, 2]:
            if column in [0, 1, 2]:
                key = 1
            elif column in [3, 4, 5]:
                key = 2
            else:
                key = 3
        elif row in [3, 4, 5]:
            if column in [0, 1, 2]:
                key = 4
            elif column in [3, 4, 5]:
                key = 5
            else:
                key = 6
        else:
            if column in [0, 1, 2]:
                key = 7
            elif column in [3, 4, 5]:
                key = 8
            else:
                key = 9
        
        return key


    # 遍历数独，对每种数据进行初始化
    def _init(self):
        for row, row_datas in enumerate(self.sudo_ku):
            for column, value in enumerate(row_datas):
                if value == '':
                    self.vacant_position.append( (row,column) )
                else:
                    self._add_row_data(row, value)
                    self._add_column_data(column, value)
                    self._add_three_to_three_data(row, column, value)
    
    # 编写判断某一位置的值是否合法
    def _judge_value_is_legal(self, row, column, value):
        if value in self.every_row_data[row]:
            return False
        if value in self.every_column_data[column]:
            return False
        
        key = self._get_three_to_three_key(row, column)
        if value in self.every_three_to_three_data[key]:
            return False
        
        reutrn True 

    # 在当前位置循环，可以使用的数据，确定是否可以放置这个值
    def _calculate(self, vacant_position):
        row, column = vacant_position
        values = set(range(1, 10))

        key = str(row) + str(column)
        if key in self.every_vacant_position_tried_values:
            # 对values取差集，用-
            values = values - self.every_vacant_position_tried_values[key]
        else:
            self.every_vacant_position_tried_values[key] = set()
        
        for value in values:
            self.every_vacant_position_tried_values[key].add(value)

            if self._judge_value_is_legal(row, column, value):
                print(f'set {vacant_position} value is {vlaue}')
                self.every_column_data[column].add(value)
                self.every_row_data[row].add(value)
                key = self._get_three_to_three_key(row, column)
                self.every_three_to_three_data[key].add(value)
                self.sudo_ku[row][column] = value
                return True, value

        return False, None
    
    # 回溯函数
    def _backtrack(self, current_vacant_position, previous_vacant_position, previous_value):
        print(f'run backtracking... value is {previous_value}, vacant position is {previous_vacant_position} ')
        row, column = previous_vacant_position
        self.every_column_data[column].remove(previous_value)
        self.every_row_data[row].remove(previous_value)

        key = self._get_three_to_three_key(row, column)
        self.every_three_to_three_data[key].remove(previous_value)

        self.sudo_ku[row][column] = ''

        current_row, current_column = current_vacant_position
        key = str(current_row) + str(current_column)
        self.every_vacant_position_tried_values.pop(key)
    
    # 计算函数，循环所有的空缺位置
    def get_result(self):
        self._init()

        length = len(self.vacant_position)
        index = 0

        tried_values = []
        while index < length:
            vacant_position = self.vacant_position[index]
            is_success, value = self._calculate(vacant_position)
            if is_success:
                tried_values.append(value)
                index += 1
            else:
                self._backtrack(vacant_position, self.vacant_position[index-1], tried_values.pop())
            
            if index < 0:
                raise ValueError(f'{self.sudo_ku} is a invalid sudo ku')
    return self.sudo_ku

