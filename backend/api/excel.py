# -*- coding: utf-8 -*-

import xlrd  # 需要安装1.2.0版本，否则不支持xlsx
from DegreeOverView.settings import MEDIA_ROOT

# 测试用路径, 文件
# MEDIA_ROOT = 'C:\\excel\\'
# file_name = 'test.xlsx'


class ExcelImport:
    def __init__(self, file_name):
        # self.file_name = unicode(file_name, "utf-8")
        # 文件路径修改
        self.file_name = (MEDIA_ROOT + str(file_name)).replace("/", "\\").encode("utf-8").decode("utf-8")
        # print self.file_name
        self.workbook = xlrd.open_workbook(self.file_name)
        self.table = self.workbook.sheets()[0]
        # 获取总行数
        self.nrows = self.table.nrows

        self.evaluation_method = []
        self.percentage = []
        self.cilo = []

    def get_cases(self):
        # 从第二行开始
        for x in range(1, self.nrows):
            row = self.table.row_values(x)
            self.evaluation_method.append(row[0])
            self.percentage.append(row[1])
            if isinstance(row[2], float):
                row[2] = str(int(row[2]))
            self.cilo.append(row[2])
        result = [self.evaluation_method, self.percentage, self.cilo]
        print(result)
        return result

# ExcelImport(file_name).get_cases()
