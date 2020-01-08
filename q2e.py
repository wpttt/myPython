#!python3
# -*- coding: utf-8 -*-
# %%
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

window = tk.Tk()
window.title('地震目录转换--脑残版')
window.geometry('450x300+500+200')
inType = tk.StringVar()
outType = tk.StringVar()
selectedFileName = tk.StringVar()
selectedDirectory = tk.StringVar()
selectedMergeFile = tk.StringVar()
outfilename = ''
infilename = ''
mergefilename = ''
incat = ''
outcat = ''



def q2e(incatalog, outcatalog):
    # 读取Q01目录
    tab = pd.read_csv(incatalog, encoding='gbk', header=1,
                      skip_blank_lines=True, skipinitialspace=True)
    # 删除无用行
    # tab.drop(labels=[0, 1], axis=0)
    tab.drop(index=[tab.shape[0]-1], inplace=True)
    # 更改字段名
    tab.columns = ['lines']
    # 添加相关时间、纬度、经度、震级、深度、地名等字段
    tab['time'] = tab.apply(lambda x: x.lines[:14], axis=1)
    tab['lat'] = tab.apply(lambda x: x.lines[16:19] + '.' +
                           str('%.2f' % (float(x.lines[19:21])/60))[-2:],
                           axis=1)
    tab['lon'] = tab.apply(lambda x: x.lines[21:25] + '.' +
                           str('%.2f' % (float(x.lines[25:27])/60))[-2:],
                           axis=1)
    tab['mag'] = tab.apply(lambda x: x.lines[30:33] + '0', axis=1)
    tab['dep'] = tab.apply(lambda x: x.lines[34:37] + '000', axis=1)
    tab['loc'] = tab.apply(lambda x: x.lines[43:], axis=1)
    # 添加eqt格式列
    tab['eqt'] = tab.apply(lambda x:
                           x.time.rjust(15, ' ') +
                           x.lat.rjust(6, ' ') +
                           x.lon.rjust(7, ' ') +
                           x.mag +
                           x.dep.rjust(6, ' ') + ' ' +
                           x['loc'],
                           axis=1)
    # 将eqt格式列保存至文件
    tab.to_csv(outcatalog, encoding='gbk',
               columns=['eqt'], header=False, index=False)


def incatalog_selection():    # 创建command函数，获取输入数据类型
    global incat
    incat = inType.get()


def outcatalog_selection():    # 创建command函数，获取输出数据类型
    global outcat
    outcat = outType.get()


def selectFile():
    global infilename
    infilename = askopenfilename()
    selectedFileName.set(infilename)


def selectDirectory():
    global outfilename
    global outcat
    outfilename = askdirectory() + '/outputfile.EQT'
    selectedDirectory.set(outfilename)


def selectMergeFile():
    global mergefilename
    mergefilename = askopenfilename()
    selectedMergeFile.set(mergefilename)


def warninggg():
    tk.messagebox.showwarning('警告', '请选择输入数据格式、输出格式、输入文件及合并文件或输出路径')


def tansformCatalog():   # show varay
    global outfilename
    global infilename
    global mergefilename
    global incat
    global outcat
    if incat == '' or outcat == '' or infilename == '' or outfilename == '':
        print("showwarning:", tk.messagebox.showwarning('警告', '请选择输入数据格式、输出格式、输入文件及合并文件或输出路径'))
        # if mergefilename == '':
    #     q2e(infilename, outfilename)
    else:
        q2e(infilename, outfilename)


# 创建输入输出数据类型标签
tk.Label(window, bg='ghostwhite', text='请选择输入数据格式（请选择Q01，因为其他选项选了也没用）').place(x=30, y=20)
tk.Label(window, bg='ghostwhite', text='请选择输出数据格式（请选择EQT，因为其他选项选了也没用）').place(x=30, y=80)
# test
# ln = tk.Label(window, text='变量测试', width=50)
# ln.place(x=0, y=0)
# 创建输入格式单选选项
tk.Radiobutton(window, text='Q01', variable=inType, value='Q01', command=incatalog_selection).place(x=50, y=50)
tk.Radiobutton(window, text='EQT', variable=inType, value='EQT', command=incatalog_selection).place(x=180, y=50)
tk.Radiobutton(window, text='C62', variable=inType, value='C62', command=incatalog_selection).place(x=310, y=50)
# 创建输出格式单选选项
tk.Radiobutton(window, text='Q01', variable=outType, value='Q01', command=outcatalog_selection).place(x=50, y=110)
tk.Radiobutton(window, text='EQT', variable=outType, value='EQT', command=outcatalog_selection).place(x=180, y=110)
tk.Radiobutton(window, text='C62', variable=outType, value='C62', command=outcatalog_selection).place(x=310, y=110)
# 创建选择输入文件标签、输入框、按钮
tk.Label(window, bg='ghostwhite', text='待转换目录:').place(x=30, y=160)
tk.Entry(window, width=25, textvariable=selectedFileName).place(x=120, y=160)
tk.Button(window, text='...', command=selectFile).place(x=360, y=160)
# 创建选择输出文件标签、输入框、按钮
tk.Label(window, bg='ghostwhite', text='输出目录至:').place(x=30, y=190)
tk.Entry(window, width=25, textvariable=selectedDirectory).place(x=120, y=190)
tk.Button(window, text='...', command=selectDirectory).place(x=360, y=190)
# 创建选择合并文件标签、输入框、按钮
tk.Label(window, bg='ghostwhite', text='合并目录至:').place(x=30, y=220)
tk.Entry(window, width=25, textvariable=selectedMergeFile).place(x=120, y=220)
tk.Button(window, text='...', command=selectMergeFile).place(x=360, y=220)
# 添加转换按钮
tk.Button(window, text='脑残转换', command=tansformCatalog).place(x=80, y=260)
# 添加合并按钮
tk.Button(window, text='转换&合并', command=warninggg).place(x=180, y=260)
# 添加取消按钮
tk.Button(window, text='取消', command=window.quit).place(x=290, y=260)

window.mainloop()
