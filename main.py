import tkinter
from tkinter import *
import cyberliuyao
import warehouse


class Application(Frame):
    """将GUI封装成类"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tkinter.BOTH, expand=True)
        """实例变量"""
        self.toss = None
        self.bengua = None
        self.biangua = None
        self.benGG = None
        self.bianGG = None
        self.benNJ = None
        self.bianNJ = None
        self.benLQ = None
        self.bianLQ = None
        self.queLQ = None
        self.liushen = None
        self.yuejian = None
        self.richen = None
        """实例变量"""
        self.creatWidge()

    def creatWidge(self):
        """创建组件"""
        # 定义组件
        self.btnPG = Button(self, text="排挂", command=self.execute)

        # 布局组件
        self.btnPG.place(relx=0.88, rely=0.2, y=-20)

    def showGuaxiang(self, bengua, biangua):
        """
        :param bengua: 1*6的布尔矩阵
        :param biangua: 1*6的布尔矩阵
        :return: 没有返回值，用不同的label显示卦象的图形
        """

        self.clear_labels()
        bengua = tuple(bengua.reshape(-1))
        biangua = tuple(biangua.reshape(-1))

        # 本卦
        text_bengua_b_zi = warehouse.BaGua[bengua[:3]]
        text_bengua_b = warehouse.BGtuxiang[text_bengua_b_zi]
        text_bengua_t_zi = warehouse.BaGua[bengua[3:6]]
        text_bengua_t = warehouse.BGtuxiang[text_bengua_t_zi]

        # 变卦
        text_biangua_b_zi = warehouse.BaGua[biangua[:3]]
        text_biangua_b = warehouse.BGtuxiang[text_biangua_b_zi]
        text_biangua_t_zi = warehouse.BaGua[biangua[3:6]]
        text_biangua_t = warehouse.BGtuxiang[text_biangua_t_zi]

        # 定义组件
        label_ben = Label(self, font=("黑体", 20), text="本卦")
        label_bian = Label(self, font=("黑体", 20), text="变卦")
        label_yjrc = Label(self, font=("黑体", 25),
                           text="月建：" + self.yuejian + "               " + "日辰：" + self.richen
                           , relief="groove")
        label_ben_b = Label(self, font=("黑体", 80))
        label_ben_b_zi = Label(self, font=("黑体", 20))
        label_bian_b = Label(self, font=("黑体", 80))
        label_bian_b_zi = Label(self, font=("黑体", 20))
        label_ben_t = Label(self, font=("黑体", 80))
        label_ben_t_zi = Label(self, font=("黑体", 20))
        label_bian_t = Label(self, font=("黑体", 80))
        label_bian_t_zi = Label(self, font=("黑体", 20))
        label_liushen = Label(self, font=("黑体", 14))
        label_benLQ = Label(self, font=("黑体", 14))
        label_bianLQ = Label(self, font=("黑体", 14))
        label_benS = Label(self, font=("黑体", 14), text="世")
        label_bianS = Label(self, font=("黑体", 14), text="世")
        label_benY = Label(self, font=("黑体", 14), text="应")
        label_bianY = Label(self, font=("黑体", 14), text="应")

        # 赋值
        label_ben_b["text"] = text_bengua_b
        label_ben_b_zi["text"] = text_bengua_b_zi
        label_ben_t["text"] = text_bengua_t
        label_ben_t_zi["text"] = text_bengua_t_zi
        label_bian_b["text"] = text_biangua_b
        label_bian_b_zi["text"] = text_biangua_b_zi
        label_bian_t["text"] = text_biangua_t
        label_bian_t_zi["text"] = text_biangua_t_zi
        label_liushen["text"] = (
                self.liushen[5] + "\n\n" + self.liushen[4] + "\n\n" + self.liushen[3] + "\n\n" + self.liushen[2]
                + "\n\n" + self.liushen[1] + "\n\n" + self.liushen[0]
        )
        label_benLQ["text"] = (
                self.benLQ[5] + self.benNJ[5] + "\n\n" + self.benLQ[4] + self.benNJ[4] + "\n\n" + self.benLQ[3]
                + self.benNJ[3] + "\n\n" + self.benLQ[2] + self.benNJ[2] + "\n\n" + self.benLQ[1] + self.benNJ[1]
                + "\n\n" + self.benLQ[0] + self.benNJ[0]
        )
        label_bianLQ["text"] = (
                self.bianLQ[5] + self.bianNJ[5] + "\n\n" + self.bianLQ[4] + self.bianNJ[4] + "\n\n" + self.bianLQ[3]
                + self.bianNJ[3] + "\n\n" + self.bianLQ[2] + self.bianNJ[2] + "\n\n" + self.bianLQ[1] + self.bianNJ[1]
                + "\n\n" + self.bianLQ[0] + self.bianNJ[0]
        )

        # 布局
        label_bianS.pack_forget()
        label_benS.pack_forget()
        label_bianY.pack_forget()
        label_benY.pack_forget()
        label_yjrc.place(relx=0.15, rely=0.08)
        label_ben.place(relx=0.168, rely=0.78)
        label_bian.place(relx=0.57, rely=0.78)
        label_ben_b.place(relx=0.14, rely=0.5)
        label_ben_b_zi.place(relx=0.065, rely=0.61)
        label_ben_t.place(relx=0.14, rely=0.216)
        label_ben_t_zi.place(relx=0.065, rely=0.31)
        label_bian_b.place(relx=0.54, rely=0.5)
        label_bian_b_zi.place(relx=0.51, rely=0.61)
        label_bian_t.place(relx=0.54, rely=0.216)
        label_bian_t_zi.place(relx=0.51, rely=0.31)
        label_liushen.place(relx=0.1, rely=0.23)
        label_benLQ.place(relx=0.25, rely=0.23)
        label_bianLQ.place(relx=0.65, rely=0.23)
        label_benS.place(x=360, y=92 + 38 * (6 - self.benGG[1]))
        label_bianS.place(x=760, y=92 + 38 * (6 - self.bianGG[1]))
        label_benY.place(x=360, y=92 + 38 * (6 - self.benGG[2]))
        label_bianY.place(x=760, y=92 + 38 * (6 - self.bianGG[2]))

    def execute(self):
        my = cyberliuyao.LiuYao()
        self.toss = my.getToss()
        self.bengua = my.getBenGua()
        self.biangua = my.getBianGua()
        self.benGG = my.getGuaGongAndShi(self.bengua)
        self.bianGG = my.getGuaGongAndShi(self.biangua)
        self.benNJ = my.getNaJia(self.bengua)
        self.bianNJ = my.getNaJia(self.biangua)
        self.benLQ = my.getLiuQin(self.benGG[0], self.benNJ)
        self.bianLQ = my.getLiuQin(self.bianGG[0], self.bianNJ)
        self.queLQ = my.getQueLiuQin(self.bengua)
        self.liushen = my.getLiuShen()
        self.yuejian = my.yuejian
        self.richen = my.richen
        self.showGuaxiang(self.bengua, self.biangua)

    def clear_labels(self):
        """
        删除frame中的所有Label
        :param frame: 要清除Label的Frame对象
        """
        # 假设我们有一个列表来跟踪所有的Label
        # 但在这个例子中，我们将通过遍历和检查来模拟
        labels_to_remove = []
        for widget in self.winfo_children():
            if widget.winfo_class() == 'Label':
                labels_to_remove.append(widget)
        for label in labels_to_remove:
            label.destroy()


root = Tk()
root.geometry("1000x400+500+300")
root.title("赛博六爻")
app = Application(master=root)

root.mainloop()
