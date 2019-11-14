#! python3
# -*- coding:GBK -*-
"""
说明：
    本程序用于对固定格式的地震目录dataFrame计算并添加农历日期，并判断是否为调制日
    dataFrame格式为: 年 月 日 时 分 秒 纬度 经度 震级 深度 台站参数 发震地名
    程序会向后添加两列，分别为农历日期和是否调制，是否调制用y、n表示
    并范围最终的dataFrame
"""

import lunar
import readEqcat


class mOrNot():

    def ynrm(self, nl):
        mday = [
            '初一', '初二', '初八', '初九', '十五',
            '十六', '十七', '廿二', '廿三', '廿四',
            '廿五', '廿八', '廿九', '三十'
        ]
        if nl in mday:
            return 'y'
        else:
            return 'n'

    def makenl(self, eqcat):
        eqcat['nldate'] = eqcat.apply(lambda x: lunar.run(x.year, x.month, x.day), axis=1)
        eqcat['yn'] = eqcat.apply(lambda x: self.ynrm(x.nldate[-2:]), axis=1)
        return eqcat


if __name__ == "__main__":
    eqcatname = './Rm2019.txt'
    eqcat = readEqcat.formatCat(eqcatname)
    eqcat2 = mOrNot.makenl(eqcat)
    print(eqcat2.head())
