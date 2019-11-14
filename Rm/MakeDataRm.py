#! python3
# -*- coding:GBK -*-
"""
˵����
    ���������ڶԹ̶���ʽ�ĵ���Ŀ¼dataFrame���㲢���ũ�����ڣ����ж��Ƿ�Ϊ������
    dataFrame��ʽΪ: �� �� �� ʱ �� �� γ�� ���� �� ��� ̨վ���� �������
    ��������������У��ֱ�Ϊũ�����ں��Ƿ���ƣ��Ƿ������y��n��ʾ
    ����Χ���յ�dataFrame
"""

import lunar
import readEqcat


class mOrNot():

    def ynrm(self, nl):
        mday = [
            '��һ', '����', '����', '����', 'ʮ��',
            'ʮ��', 'ʮ��', 'إ��', 'إ��', 'إ��',
            'إ��', 'إ��', 'إ��', '��ʮ'
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
