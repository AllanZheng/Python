import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

from StockAnalysis import data_struct
import yfinance as yf




def GetData(startdate,enddate,code):
    param = {
        'code': code,
        'type': type,
        'startDate':startdate,
        'endDate':enddate,
        'stockType':0,
    }
    syspath = sys.path[0]
    filename = syspath+"\\data\\"+startdate+"-"+enddate+"-"+code+".csv"
    f =open(filename,"r",encoding='utf-8-sig')
    # if f==None:
    resdata = yf.download(code, start=startdate, end=enddate, progress=False)
    # else:
    #     read
    DataList = []
    f = open(filename,'w+',encoding='utf-8-sig')
    writer = csv.writer(f)
    writer.writerow("股票代码,交易日,开盘价,收盘价,最高价,最低价,成交量".split(","))
    for i in resdata.itertuples():
        column = []
        column.append(code)
        for j in i:
            column.append(j)
        writer.writerow(column)
        record = data_struct.stockdata(column[1].weekday(),True,column[0],"",column[1])
        if float(column[3])-float(column[2])>0.0:
            record.IsIncrease = True
        else:
            record.IsIncrease = False
        DataList.append(record)
    f.close()
    name = startdate+"-"+enddate+"-"+code
    return DataList,name

#统计与画图
def SatisticWeekDay(data:[data_struct.stockdata],name:str):
    Weekday =("Mon","Tue","Wed","Thur","Fri")
    IncRes =[0,0,0,0,0]
    DescRes =[0,0,0,0,0]
    if len(data)<=0:
        return
    for i in data:
        if i.IsIncrease:
            IncRes[i.Weekday]+=1
        else:
            DescRes[i.Weekday]+=1
    bar_width = 0.3  # 条形宽度
    Inc = np.arange(len(IncRes))  # 涨的横坐标
    Desc = Inc + bar_width  # 跌的横坐标
    plt.rcParams['font.sans-serif'] = 'simhei'
    # 使用两次 bar 函数画出两组条形图
    plt.bar(Inc, height=IncRes, width=bar_width, color='r', label='涨')
    plt.bar(Desc, height=DescRes, width=bar_width, color='g', label='跌')
    plt.legend()  # 显示图例
    for i in range(len(IncRes)):
        plt.text(Inc[i]-0.1, IncRes[i] + IncRes[i]/30, "%s" % IncRes[i],va ='center')
    for i in range(len(DescRes)):
        plt.text(Desc[i]-0.1, DescRes[i] + DescRes[i]/30, "%s" % DescRes[i],va = 'center')
    plt.xticks(Inc + bar_width / 2, Weekday)  # 让横坐标轴刻度显示星期， Inc + bar_width / 2 为横坐标轴刻度的位置
    plt.ylabel('天数')  # 纵坐标轴标题
    title = name+'星期涨跌统计'
    plt.title(title)
    jpgfilename = './'+'graph'+'\\'+name+'.jpg'
    plt.savefig(jpgfilename)
    plt.show()
    return


dji_data,name = GetData('2010-01-01','2021-01-05','DJI')
SatisticWeekDay(dji_data,name)
ndx_data = yf.download('NDX', start='2021-01-01', end='2021-01-01', progress=False)
#spx_data = yf.download('SPX', start='2020-01-01', end='2021-01-01', progress=False)
