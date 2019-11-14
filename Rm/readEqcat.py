# readEqcat.py
"""
说明:
    本程序用于地震目录的读取和转换，并返回固定格式的dataFrame数据
    返回dataFrame格式为：年 月 日 时 分 秒 纬度 经度 震级 深度 台站参数 发震地名
    输入格式:1. eqt     需要带路径的地震目录文件名
            2. Q01      需要带路径的地震目录文件名
    程序根据文件名后缀自行判断输入文件格式，并将其按照以上固定格式输出
"""
import pandas as pd


class readEqcat():

    def readEqt(eqcat):    # eqcat为dataFrame
        eqcat['year'] = eqcat.apply(lambda x: int(x[0][0:5]), axis=1)
        eqcat['month'] = eqcat.apply(lambda x: int(x[0][5:7]), axis=1)
        eqcat['day'] = eqcat.apply(lambda x: int(x[0][7:9]), axis=1)
        eqcat['hour'] = eqcat.apply(lambda x: int(x[0][9:11]), axis=1)
        eqcat['minute'] = eqcat.apply(lambda x: int(x[0][11:13]), axis=1)
        eqcat['second'] = eqcat.apply(lambda x: float(x[0][13:15]), axis=1)
        eqcat['latitude'] = eqcat.apply(lambda x: float(x[0][15:21]), axis=1)
        eqcat['longitude'] = eqcat.apply(lambda x: float(x[0][21:28]), axis=1)
        eqcat['magnitude'] = eqcat.apply(lambda x: float(x[0][28:32]), axis=1)
        eqcat['depth'] = eqcat.apply(lambda x: int(x[0][32:36]), axis=1)
        eqcat['station'] = eqcat.apply(lambda x: x[0][36:39], axis=1)
        eqcat['location'] = eqcat.apply(lambda x: x[0][40:], axis=1)
        return eqcat


    def readQ01(eqcat):  # eqcat为dataFrame
        eqcat['year'] = eqcat.apply(lambda x: int(x[0][0:4]), axis=1)
        eqcat['month'] = eqcat.apply(lambda x: int(x[0][4:6]), axis=1)
        eqcat['day'] = eqcat.apply(lambda x: int(x[0][6:8]), axis=1)
        eqcat['hour'] = eqcat.apply(lambda x: int(x[0][8:10]), axis=1)
        eqcat['minute'] = eqcat.apply(lambda x: int(x[0][10:12]), axis=1)
        eqcat['second'] = eqcat.apply(lambda x: float(x[0][12:16]), axis=1)
        eqcat['latitude'] = eqcat.apply(
            lambda x: float(x[0][17:19]) +
            round(float(x[0][19:21]) / 60, 2),
            axis=1
        )
        eqcat['longitude'] = eqcat.apply(
            lambda x: float(x[0][22:25]) +
            round(float(x[0][25:27]) / 60, 2),
            axis=1
        )
        eqcat['magnitude'] = eqcat.apply(lambda x: float(x[0][30:33]), axis=1)
        eqcat['depth'] = eqcat.apply(lambda x: x[0][33:37], axis=1)
        eqcat['station'] = eqcat.apply(lambda x: x[0][37:42], axis=1)
        eqcat['location'] = eqcat.apply(lambda x: x[0][42:], axis=1)
        return eqcat

    def formatCat(self, eqcatname):
        # os.chdir('/Users/wpt/python/Rm')
        eqcat = pd.read_csv(eqcatname, sep='\n', header=None, encoding='gbk')
        eqcat.columns = ['eq']
        # if eqcat.endswith('.EQT') or eqcat.endswith('.eqt'):
        if 'ML' in eqcat['eq'][0] or 'MS' in eqcat['eq'][0]:
            catalog = self.readQ01(eqcat)
        else:
            catalog = self.readEqt(eqcat)
        formatedEqcat = catalog[[
                                'year', 'month', 'day', 'hour', 'minute',
                                'second', 'latitude', 'longitude', 'magnitude',
                                'depth', 'station', 'location'
                                ]]
        return formatedEqcat


if __name__ == "__main__":
    pass
