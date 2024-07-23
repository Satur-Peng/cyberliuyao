import numpy as np
temp = np.zeros((3, 1), bool)
Qian = np.full((3, 1), 1, bool)
Kun = np.zeros((3, 1), bool)
Dui = np.copy(Qian)
Dui[2] = False
Li = np.copy(Qian)
Li[1] = False
Zhen = np.copy(Kun)
Zhen[0] = True
Xun = np.copy(Qian)
Xun[0] = False
Kan = np.copy(Kun)
Kan[1] = True
Gen = np.copy(Kun)
Gen[2] = True
Qian = tuple(Qian.reshape(-1))
Dui = tuple(Dui.reshape(-1))
Li = tuple(Li.reshape(-1))
Zhen = tuple(Zhen.reshape(-1))
Xun = tuple(Xun.reshape(-1))
Kan = tuple(Kan.reshape(-1))
Gen = tuple(Gen.reshape(-1))
Kun = tuple(Kun.reshape(-1))
BaGua = {Qian: "乾", Dui: "兑", Li: "离", Zhen: "震", Xun: "巽", Kan: "坎", Gen: "艮", Kun: "坤"}
BGyingyang = {"阴": (Dui, Li, Xun, Kun), "阳": (Qian, Kan, Gen, Zhen)}
TianGan = ("甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸")
Dizhi = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥")
NaJia = {("乾", 0): ("甲", "子"), ("乾", 1): ("壬", "午"), ("坎", 0): ("戊", "寅"), ("坎", 1): ("戊", "申")
         , ("震", 0): ("庚", "子"), ("震", 1): ("庚", "午"), ("艮", 0): ("丙", "辰"), ("艮", 1): ("丙", "戌")
         , ("坤", 0): ("乙", "未"), ("坤", 1): ("癸", "丑"), ("巽", 0): ("辛", "丑"), ("巽", 1): ("辛", "未")
         , ("离", 0): ("己", "卯"), ("离", 1): ("己", "酉"), ("兑", 0): ("丁", "巳"), ("兑", 1): ("丁", "亥")}
BGwuxing = {"乾": "金", "兑": "金", "离": "火", "震": "木", "巽": "木", "坎": "水", "艮": "土", "坤": "土"}
DZwuxing = {"子": "水", "丑": "土", "寅": "木", "卯": "木", "辰": "土", "巳": "火", "午": "火", "未": "土", "申": "金",
            "酉": "金", "戌": "土", "亥": "水"}
WuXing = ("金", "水", "木", "火", "土")
LiuQing = {-2: "官鬼", -1: "父母", 0: "兄弟", 1: "子孙", 2: "妻财"}
QingLS = {"甲": "青龙", "乙": "青龙", "丙": "朱雀", "丁": "朱雀", "戊": "勾陈", "己": "腾蛇", "庚": "白虎", "辛": "白虎",
          "壬": "玄武", "癸": "玄武"}
LiuShen = ("青龙", "朱雀", "勾陈", "腾蛇", "白虎", "玄武")
BGtuxiang = {"乾": "☰", "坤": "☷", "震": "☳", "巽": "☴", "坎": "☵", "离": "☲", "艮": "☶", "兑": "☱"}