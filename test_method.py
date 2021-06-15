# import csv
#
# rows = []
# # open the CSV file
# data_file = open('testdata.csv',encoding = 'utf-8')
# # create a CSV Reader from CSV file
# reader = csv.reader(data_file)
# print(reader)
# # skip the headers
# next(reader, None)
# # add rows from reader to list
# for row in reader:
#     rows.append(row)
# print(rows)


# import xlrd
#
# # create an empty list to store rows
# rows = []
# # open the specified Excel spreadsheet as workbook
# book = xlrd.open_workbook('TestData.xls')
# # get the first sheet
# sheet = book.sheet_by_index(0)
# # iterate through the sheet and get data from rows in list
# print(sheet)
# print(range(1, sheet.nrows))
# for row_idx in range(1, sheet.nrows):
#     rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
# print(rows)
#
# import sys
# print (sys.path)

#
# from subprocess import PIPE, Popen
# # 返回的是 Popen 实例对象
# proc = Popen(
#     'fsutil volume diskfree c:',
#     stdin  = None,
#     stdout = PIPE,
#     stderr = PIPE,
#     shell=True)
#
# # communicate 方法返回 输出到 标准输出 和 标准错误 的字节串内容
# # 标准输出设备和 标准错误设备 当前都是本终端设备
# outinfo, errinfo = proc.communicate()
#
# # 注意返回的内容是bytes 不是 str ，我的是中文windows，所以用gbk解码
# outinfo = outinfo.decode('gbk')
# errinfo = errinfo.decode('gbk')
# print (outinfo)
# print ('-------------')
# print (errinfo)
#
# outputList = outinfo.splitlines()
#
# # 剩余量
# free  = int(outputList[0].split(':')[1].strip())
#
# # 总空间
# total = int(outputList[1].split(':')[1].strip())
#
# if (free/total < 0.1):
#     print('!! 剩余空间告急！！')
# else:
#     print('剩余空间足够')

#
# #测试创建新线程
# print('主线程执行代码')
#
# # 从 threading 库中导入Thread类
# from threading import Thread
# from time import sleep
#
# # 定义一个函数，作为新线程执行的入口函数
# def threadFunc(arg1,arg2):
#     print('子线程 开始')
#     print(f'线程函数参数是：{arg1}, {arg2}')
#     sleep(5)
#     print('子线程 结束')
#
#
# # 创建 Thread 类的实例对象， 并且指定新线程的入口函数
# thread = Thread(target=threadFunc,
#                 args=('参数1', '参数2')
#                 )
#
# # 执行start 方法，就会创建新线程，
# # 并且新线程会去执行入口函数里面的代码。
# # 这时候 这个进程 有两个线程了。
# thread.start()
#
# # 主线程的代码执行 子线程对象的join方法，
# # 就会等待子线程结束，才继续执行下面的代码
# thread.join()
# print('主线程结束')


#daemon线程
# from threading import Thread
# from time import sleep
#
# def threadFunc():
#     sleep(2)
#     print('子线程 结束')
#
# thread = Thread(target=threadFunc)
# thread.start()
# # print('主线程结束')
# from threading import Thread
# from time import sleep
#
# def threadFunc():
#     sleep(2)
#     print('子线程 结束')
#
# thread = Thread(target=threadFunc,
#                 daemon=True # 设置新线程为daemon线程
#                 )
# thread.start()
# print('主线程结束')


#正则表达式
# content = '''张三，手机号码15945678901
# 李四，手机号码13945677701
# 王二，手机号码13845666901'''
#
# import re
# p = re.compile(r'^(.+)，.+(\d{11})', re.MULTILINE)
# for one in  p.findall(content):
#     print(one)
content = '''张三，手机号码15945678901
李四，手机号码13945677701
王二，手机号码13845666901'''

import re
p = re.compile(r'^(?P<name>.+)，.+(?P<phone>\d{11})', re.MULTILINE)
for match in  p.finditer(content):
    print(match.group('name'))
    print(match.group('phone'))