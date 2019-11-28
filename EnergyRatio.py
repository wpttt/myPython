#! python
# -*- coding:utf-8 -*-
"""
This grogram used to calculate the Energy Ratio of the main earthquake in the sequence.
And it will print the result onto the Standard Output or write the result into a text file .

How To Call:
    1. With CMD: python Er.py 'earthquake catalog with EQT format' input-file output-file,
        print the result onto Standard Output and write the result into output-file
    2. As a module: import EnergyRatio as er, then er.energy_R('input-file')
        print the result onto Standard output and return the result
"""

import sys
import pandas as pd

# class e_R(object):
    ## 读取传入文件为DataFrame
def eq_Energy(mag):
    exponent = 1.5 * mag + 11.8
    energy = 10 ** exponent
    return energy


def energy_R(file):
    df = pd.read_csv(file, names=['eq'], encoding='gbk')
    # print('Read data below：\n', df.head())  # 打印读取结果
    df['mag'] = df.apply(lambda x: x['eq'][28:32], axis=1)
    df['energy'] = df.apply(lambda x: eq_Energy(float(x.mag)), axis=1)
    m_max = max(df.mag)
    e_max = eq_Energy(float(m_max))
    e_sum = sum(df.energy)
    e_r = e_max / e_sum
    print(str(round(e_r*100, 2)) + '%')
    return e_r


if __name__ == "__main__":
    ## 设置变量的接收方式，为python name.py 输入文件 输出文件
    infile = sys.argv[1]
    outfile = sys.argv[2]
	#print(energy_R(infile))
    with open(outfile, 'w') as f:
        f.write(str(energy_R(infile)))
