import os

DATA_PATH = "data/chat_data.xlsx"

import xlrd  
  
def row2str(row_data):  
    values = "";  
    for i in range(len(row_data)):  
        if i == len(row_data) - 1:  
            values = values + str(row_data[i])  
        else:  
            values = values + str(row_data[i]) + "|"  
    return values  
  
  
# 打开文件  
try:  
    data = xlrd.open_workbook(DATA_PATH)  
except:  
    print("fail to open file")  
else:  
    # 文件读写方式是追加  
    file = open("data/chat_data.txt", "w")  
    # 表头  
    table = data.sheets()[0]  
    # 行数  
    row_cnt = table.nrows  
    # 列数  
    col_cnt = table.ncols  
    # 打印出行数列数  
    print(row_cnt)  
    print(col_cnt)   
    for j in range(0, row_cnt):  
        row = table.row_values(j)  
        # 调用函数，将行数据拼接成字符串  
        row_values = row2str(row)  
        # 将字符串写入新文件  
        file.write(row_values + "\n")  
    # 关闭写入的文件  
    file.close()  
