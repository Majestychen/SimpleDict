# -*- coding: utf-8 -*-

from tkinter import *
import urllib.request as ur
from urllib.parse import quote
import json
import types



root = Tk()
root.title('MyDict')
root.geometry('500x500')
root.resizable(width=True, height=False)

#数据设置到列表
def setData(listData):
    resultList.delete(0,END)
    if isinstance(listData,list):
        for item in listData:
            resultList.insert(END,item['pos']+'   '+item['def'])
    else:
        resultList.insert(END,listData)        

#api查询数据
def queryDict(word):
    url = 'http://xtk.azurewebsites.net/BingDictService.aspx?Word='+quote(word)
    with ur.urlopen(url) as f:
        listData = f.read().decode()
        try:
            module = json.loads(listData)['defs']
            setData(module)
        except ValueError as e:
            setData(listData)

#输入框布局
inputFrame = Frame(root,height = 15)
#输入框
entry = Entry(inputFrame,width=30,font=10) 
entry.pack(side=LEFT,padx = 20,pady = 50)
#按钮
button = Button(inputFrame, text = '查询',command = lambda: queryDict(entry.get()))
button.pack(side=LEFT)
inputFrame.pack(expand = NO,fill = X)

#查询结果布局
resultFrame = Frame(root,height = 300,width=400,bg='white')
#列表
resultList = Listbox(resultFrame)
resultList.pack(fill=BOTH,expand = NO)

resultFrame.pack(fill=BOTH,expand = NO,padx = 20)

root.mainloop()