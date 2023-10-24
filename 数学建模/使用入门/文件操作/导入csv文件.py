#研发者：时间遗忘
#开发时间：2023/8/14 22:30
'''
1、通过标准的Python库导入CSV文件：

Python提供了一个标准的类库CSV文件。这个类库中的reader()函数用来导入CSV文件。当CSV文件被读入后，可以利用这些数据生成一个NumPy数组，用来训练算法模型。：
'''

from csv import reader

import numpy as np

filename=input("请输入文件名： ")

with open(filename,'rt',encoding='UTF-8')as raw_data:

  readers=reader(raw_data,delimiter=',')

  x=list(readers)

  data=np.array(x)

  print(data)

  print(data.shape)

'''
开始处导入了所需的模块：csv用于读取CSV文件，numpy用于创建和操作数组。

filename变量通过input函数从用户获取输入的文件名。

使用open函数打开指定的文件，并使用with语句创建一个上下文管理器，确保文件在使用完后正确关闭。

reader函数用于创建一个CSV文件的读取器对象，它接收文件对象和分隔符作为参数。在这里，我们将分隔符设置为逗号(delimiter=',')。

list(readers)将读取器对象转换为一个列表，并将每行数据作为一个字符串列表包含在其中。这个列表被赋值给变量x。

使用NumPy的array函数将列表x转换为NumPy数组，将结果存储在变量data中。

print(data)打印出数组data，显示CSV文件的全部数据。

print(data.shape)打印出数组data的形状。形状以元组的形式表示，其中第一个元素是行数，第二个元素是列数。

请注意，代码中的文件名输入部分使用的是input函数，这意味着在运行代码时，您需要手动输入要读取的CSV文件的名称。确保文件在当前工作目录中存在，并输入正确的文件名以正确读取和处理数据。
'''

'''
2、通过NumPy导入CSV文件

也可以使用NumPy的loadtxt()函数导入数据。使用这个函数处理的数据没有文件头，并且所有的数据结构都是一样的，也就是说，数据类型是一样的。
'''
from numpy import loadtxt

filename=input("文件名：")

with open(filename,'rt',encoding='UTF-8')as raw_data:

  data=loadtxt(raw_data,delimiter=',')

  print(data)
'''
from numpy import loadtxt导入了NumPy库中的loadtxt函数，该函数用于从文本文件加载数据。

filename通过input函数从用户获取输入的文件名。

使用open函数打开指定的文件，并使用with语句创建一个上下文管理器，确保文件在使用完后正确关闭。

loadtxt函数接收文件对象和分隔符作为参数，并从文件中加载数据。这里将文件对象raw_data和分隔符,传递给loadtxt函数进行数据加载。

加载的数据被存储在变量data中，以NumPy数组的形式表示。

print(data)打印出数组data，显示CSV文件中的全部数据。

请注意，在使用这段代码之前，请确保您已经安装了NumPy库。此外，与之前的代码示例一样，请确保输入的文件名有效，并在当前工作目录中存在。文件应该是一个逗号分隔的文本文件，且内容应该与NumPy数组的格式兼容。
'''

'''
3、通过Pandas导入CSV文件

通过Pandas来导入CSV文件要使用pandas.read_csv()函数。这个函数的返回值是DataFrame，可以很方便的进行下一步的处理，实际操作过程中推荐使用这种方法。

在机器学习的项目中，经常利用Pandas来做数据清洗与数据准备工作。
'''

from pandas import read_csv

filename=input("文件名：")

f=open(filename,encoding='UTF-8')

names=['作业日期','ηCO','ηH2','TF(℃)','TC(℃)','mass','送风流量']

data=read_csv(f,names=names)

print(data)

'''
使用from pandas import read_csv导入了Pandas库中的read_csv函数，用于读取CSV文件。

filename通过input函数从用户获取输入的文件名。

通过使用open函数打开指定的文件，并将返回的文件对象赋给变量f。我们指定了encoding='UTF-8'来确保以UTF-8编码打开文件。

创建了一个名为names的列表，其中包含CSV文件中每列数据的名称。

使用read_csv函数读取文件对象f中的数据。names=names参数指定了列名，以确保正确地将每列数据与对应的列名关联。

读取的数据被存储在一个DataFrame对象data中。

使用print(data)打印出DataFrame对象data，显示CSV文件中的全部数据。

请注意，在使用这段代码之前，请确保您已经安装了Pandas库。此外，与之前的示例一样，请确保输入的文件名有效，并在当前工作目录中存在。CSV文件中的数据应该与提供的列名对应，并且以逗号分隔。

'''
