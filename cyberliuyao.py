import random
import numpy as np
import requests
import warehouse
from datetime import datetime

Decode = {""}


class LiuYao:
    def __init__(self):
        self.Toss = None
        self.BianGua = None
        self.BenGua = None
        self.countLQ = []
        self.yuejian = None
        self.richen = None

    # 输入无
    def getToss(self):
        self.Toss = np.zeros((6, 3))
        for i in range(6):
            self.Toss[i - 1] = (np.random.rand(3) >= 0.5)
        return self.Toss

    # 输出一个3*6的布尔值矩阵，会更改类属性值Toss

    # 输入无
    def getBenGua(self):
        self.BenGua = np.zeros((6, 1), bool)
        for i in range(6):
            Count = int(self.Toss[i][0]) + int(self.Toss[i][1]) + int(self.Toss[i][2])
            if Count > 1:
                self.BenGua[i] = True
            else:
                self.BenGua[i] = False
        return self.BenGua

    # 输出1*6的布尔矩阵，会更改类属性值BenGua

    # 输入无
    def getBianGua(self):
        self.BianGua = np.zeros((6, 1), bool)
        for i in range(6):
            Count = int(self.Toss[i][0]) + int(self.Toss[i][1]) + int(self.Toss[i][2])
            if Count in (0, 2):
                self.BianGua[i] = True
            else:
                self.BianGua[i] = False
        return self.BianGua

    # 输出1*6的布尔矩阵，会更改类属性值BianGua

    # 输入无
    def getGuaGongAndShi(self, Gua):
        Count = np.zeros((3, 1), bool)
        for i in range(3):
            if Gua[i] == Gua[i + 3]:
                Count[i] = True
            else:
                Count[i] = False
        if Count[2] and (not ((Count[0] + Count[1]))):
            Shi = 2
        elif (not Count[2]) and (Count[0] and Count[1]):
            Shi = 5
        elif Count[0] and (not ((Count[1] + Count[2]))):
            Shi = 4
        elif (not Count[0]) and (Count[1] and Count[2]):
            Shi = 1
        elif Count[0] and Count[1] and Count[2]:
            Shi = 6
        elif (not Count[1]) and (not Count[0]) and (not Count[2]):
            Shi = 3
        elif Count[1] and (not ((Count[0] + Count[2]))):
            Shi = 4
        else:
            Shi = 3
        if Shi > 3:
            Ying = Shi - 3
        else:
            Ying = Shi + 3
        if Count[1] and Count[2]:
            return Gua[3:6], Shi, Ying
        elif Count[2] and (not (Count[0] or Count[1])):
            return Gua[3:6], Shi, Ying
        elif not (Count[0] or Count[1] or Count[2]):
            return Gua[3:6], Shi, Ying
        elif Count[0] and (not (Count[1] or Count[2])):
            return np.logical_not(Gua[0:3]), Shi, Ying
        elif (Count[0] and Count[1]) and (not Count[2]):
            return np.logical_not(Gua[0:3]), Shi, Ying
        elif (not (Count[0] or Count[2])) and Count[1]:
            return np.logical_not(Gua[0:3]), Shi, Ying
        else:
            return Gua[0:3], Shi, Ying
        # 输出元组，（1*3矩阵, int, int）

    # 输入1*6矩阵
    def getNaJia(self, GuaXiang):
        GuaXiang = tuple(GuaXiang.reshape(-1))
        NeiGua = warehouse.BaGua[GuaXiang[:3]]
        NeiJia = warehouse.NaJia[(NeiGua, 0)]
        WaiGua = warehouse.BaGua[GuaXiang[3:6]]
        WaiJia = warehouse.NaJia[(WaiGua, 1)]
        NeiMark = warehouse.Dizhi.index(NeiJia[1])
        WaiMark = warehouse.Dizhi.index(WaiJia[1])

        if GuaXiang[:3] in warehouse.BGyingyang["阳"]:
            NeiJia = [NeiJia[0] + warehouse.Dizhi[NeiMark],
                      NeiJia[0] + warehouse.Dizhi[(NeiMark + 2) % len(warehouse.Dizhi)],
                      NeiJia[0] + warehouse.Dizhi[(NeiMark + 4) % len(warehouse.Dizhi)]]
        else:
            NeiJia = [NeiJia[0] + warehouse.Dizhi[NeiMark],
                      NeiJia[0] + warehouse.Dizhi[NeiMark - 2],
                      NeiJia[0] + warehouse.Dizhi[NeiMark - 4]]
        if GuaXiang[3:6] in warehouse.BGyingyang["阳"]:
            WaiJia = [WaiJia[0] + warehouse.Dizhi[WaiMark],
                      WaiJia[0] + warehouse.Dizhi[(WaiMark + 2) % len(warehouse.Dizhi)],
                      WaiJia[0] + warehouse.Dizhi[(WaiMark + 4) % len(warehouse.Dizhi)]]
        else:
            WaiJia = [WaiJia[0] + warehouse.Dizhi[WaiMark],
                      WaiJia[0] + warehouse.Dizhi[WaiMark - 2],
                      WaiJia[0] + warehouse.Dizhi[WaiMark - 4]]
        NaJia = NeiJia + WaiJia
        for i in range(len(NaJia)):
            NaJia[i - 1] = NaJia[i - 1] + warehouse.DZwuxing[NaJia[i - 1][1]]
        return NaJia

    # 输出长度为6的list，全部为string

    # 输入为1*3的矩阵和长度为6的list
    def getLiuQin(self, GuaGong, NaJia):
        temp = tuple(GuaGong.reshape(-1))
        GuaGong = warehouse.BaGua[temp]
        Wo = warehouse.WuXing.index(warehouse.BGwuxing[GuaGong])
        LiuQin = []
        for i in range(len(NaJia)):
            Temp = Wo - warehouse.WuXing.index(warehouse.DZwuxing[NaJia[i - 1][1]])
            if Temp > 2:
                Temp = Temp - 5
            elif Temp < -2:
                Temp = 5 + Temp
            self.countLQ.append(Temp)
            LiuQin.append(warehouse.LiuQing[Temp])
        return LiuQin

    def getQueLiuQin(self, Gua):
        MissLQ = []
        KeyList = list(warehouse.LiuQing.keys())
        NumberYao = []
        for i in range(len(KeyList)):
            if not KeyList[i - 1] in self.countLQ:
                MissLQ.append(KeyList[i - 1])
        if not MissLQ:
            MissLQ = "不缺"
        else:
            GuaGong = self.getGuaGongAndShi(Gua)[0]
            NaJia = self.getNaJia(np.concatenate((GuaGong, GuaGong), axis=0))
            self.countLQ = []
            GuaGongLQ = self.getLiuQin(GuaGong, NaJia)
            for i in range(len(MissLQ)):
                NumberYao.append(self.countLQ.index(MissLQ[i - 1]) + 1)
                MissLQ[i - 1] = warehouse.LiuQing[MissLQ[i - 1]]
        return MissLQ, NumberYao

    def getGuaXiang(self, GuaXiang):
        GuaXiang = tuple(GuaXiang.reshape(-1))
        GuaXiang = warehouse.BaGua[GuaXiang]
        return GuaXiang

    def getLiuShen(self):
        now = datetime.now()
        url1 = "https://www.36jxs.com/api/Commonweal/almanac?"
        url2 = "sun={year}-{month}-{day}".format(year=now.year, month=now.month, day=now.day)
        url = url1 + url2
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
        r = requests.get(url=url, headers=head)
        self.richen = r.json()["data"]['TianGanDiZhiDay'][1]
        self.yuejian = r.json()["data"]['TianGanDiZhiMonth'][1]
        First = warehouse.QingLS[r.json()["data"]['TianGanDiZhiDay'][0]]
        Number = warehouse.LiuShen.index(First)
        LiuShen = []
        for i in range(Number, Number + 6):
            LiuShen.append(warehouse.LiuShen[i % 6])
        return LiuShen


# My = LiuYao()
# a = My.getToss()
# b = My.getBenGua()
# c = My.getBianGua()
# d = My.getGuaGongAndShi(b)
# e = My.getNaJia(b)
# f = My.getNaJia(c)
# g = My.getLiuQin(d[0], e)
# h = My.getQueLiuQin(b)
# i = My.getLiuShen()
# print(My.yuejian)
# print(My.yuejian, My.richen)
# print("投掷结果是", a)
# print("本卦是", b)
# print("变卦是", c)
# print("本卦卦宫是", d[0], "世是", d[1])
# print("本卦纳甲是", e)
# print("变卦纳甲是", f)
# print("六亲是", g)
# print("缺的六亲是", h)
# print("六神是", i)
