#!python3
# -*- coding: GBK -*-
# %%
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

window = tk.Tk()
window.title('����Ŀ¼ת��--�Բа�')
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
    # ��ȡQ01Ŀ¼
    tab = pd.read_csv(incatalog, encoding='gbk', header=1,
                      skip_blank_lines=True, skipinitialspace=True)
    # ɾ��������
    # tab.drop(labels=[0, 1], axis=0)
    tab.drop(index=[tab.shape[0]-1], inplace=True)
    # �����ֶ���
    tab.columns = ['lines']
    # ������ʱ�䡢γ�ȡ����ȡ��𼶡���ȡ��������ֶ�
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
    # ���eqt��ʽ��
    tab['eqt'] = tab.apply(lambda x:
                           x.time.rjust(15, ' ') +
                           x.lat.rjust(6, ' ') +
                           x.lon.rjust(7, ' ') +
                           x.mag +
                           x.dep.rjust(6, ' ') + ' ' +
                           x['loc'],
                           axis=1)
    # ��eqt��ʽ�б������ļ�
    tab.to_csv(outcatalog, encoding='gbk',
               columns=['eqt'], header=False, index=False)


def incatalog_selection():    # ����command��������ȡ������������
    global incat
    incat = inType.get()


def outcatalog_selection():    # ����command��������ȡ�����������
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
    tk.messagebox.showwarning('����', '��ѡ���������ݸ�ʽ�������ʽ�������ļ����ϲ��ļ������·��')


def tansformCatalog():   # show varay
    global outfilename
    global infilename
    global mergefilename
    global incat
    global outcat
    if incat == '' or outcat == '' or infilename == '' or outfilename == '':
        print("showwarning:", tk.messagebox.showwarning('����', '��ѡ���������ݸ�ʽ�������ʽ�������ļ����ϲ��ļ������·��'))
        # if mergefilename == '':
    #     q2e(infilename, outfilename)
    else:
        q2e(infilename, outfilename)


# ������������������ͱ�ǩ
tk.Label(window, bg='ghostwhite', text='��ѡ���������ݸ�ʽ����ѡ��Q01����Ϊ����ѡ��ѡ��Ҳû�ã�').place(x=30, y=20)
tk.Label(window, bg='ghostwhite', text='��ѡ��������ݸ�ʽ����ѡ��EQT����Ϊ����ѡ��ѡ��Ҳû�ã�').place(x=30, y=80)
# test
# ln = tk.Label(window, text='��������', width=50)
# ln.place(x=0, y=0)
# ���������ʽ��ѡѡ��
tk.Radiobutton(window, text='Q01', variable=inType, value='Q01', command=incatalog_selection).place(x=50, y=50)
tk.Radiobutton(window, text='EQT', variable=inType, value='EQT', command=incatalog_selection).place(x=180, y=50)
tk.Radiobutton(window, text='C62', variable=inType, value='C62', command=incatalog_selection).place(x=310, y=50)
# ���������ʽ��ѡѡ��
tk.Radiobutton(window, text='Q01', variable=outType, value='Q01', command=outcatalog_selection).place(x=50, y=110)
tk.Radiobutton(window, text='EQT', variable=outType, value='EQT', command=outcatalog_selection).place(x=180, y=110)
tk.Radiobutton(window, text='C62', variable=outType, value='C62', command=outcatalog_selection).place(x=310, y=110)
# ����ѡ�������ļ���ǩ������򡢰�ť
tk.Label(window, bg='ghostwhite', text='��ת��Ŀ¼:').place(x=30, y=160)
tk.Entry(window, width=25, textvariable=selectedFileName).place(x=120, y=160)
tk.Button(window, text='...', command=selectFile).place(x=360, y=160)
# ����ѡ������ļ���ǩ������򡢰�ť
tk.Label(window, bg='ghostwhite', text='���Ŀ¼��:').place(x=30, y=190)
tk.Entry(window, width=25, textvariable=selectedDirectory).place(x=120, y=190)
tk.Button(window, text='...', command=selectDirectory).place(x=360, y=190)
# ����ѡ��ϲ��ļ���ǩ������򡢰�ť
tk.Label(window, bg='ghostwhite', text='�ϲ�Ŀ¼��:').place(x=30, y=220)
tk.Entry(window, width=25, textvariable=selectedMergeFile).place(x=120, y=220)
tk.Button(window, text='...', command=selectMergeFile).place(x=360, y=220)
# ���ת����ť
tk.Button(window, text='�Բ�ת��', command=tansformCatalog).place(x=80, y=260)
# ��Ӻϲ���ť
tk.Button(window, text='ת��&�ϲ�', command=warninggg).place(x=180, y=260)
# ���ȡ����ť
tk.Button(window, text='ȡ��', command=window.quit).place(x=290, y=260)

window.mainloop()
