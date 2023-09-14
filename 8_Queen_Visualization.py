import numpy as np
import matplotlib
from matplotlib.widgets import Button
from matplotlib import pyplot as plt
import tkinter.messagebox  # 弹窗库
import tkinter as tk

matplotlib.use('TkAgg')
matplotlib.rcParams['toolbar'] = 'None'
plt.rcParams['font.family'] = 'SimHei'  # 输入中文

n = 8  # 皇后数量，默认为8
queens = np.zeros(30)  # 存放皇后结果的数组
answer_sum = 0  # 解的总数目
RR_Speed = 0.4  # 图片刷新速度

plt.subplots_adjust(bottom=0.3)  # 调整图标所在子图大小，预留出按钮的位置
fig = plt.gcf()


def check_position(row, col):  # 判断坐标为row、col的皇后是否与之前的若干皇后冲突
    i = 0
    while i < row:
        if queens[i] == col or abs(queens[i] - col) == abs(i - row):  # 若处于一列或者一条斜线上则不满足位置条件
            return 0
        else:
            i += 1
    return 1


def set_queens(index):  # 安置皇后的递归函数
    if index == n:  # 当遍历到第n个皇后时则结束函数
        plot_chess(queens)
        return 1
    else:
        i = 0
        while i < n:  # 遍历一行中的每一列8
            queens[index] = i
            if check_position(index, i):
                if index == n - 1:
                    global answer_sum
                    answer_sum += 1
                    print(queens)
                set_queens(index + 1)
            i += 1


def plot_chess(result):
    global answer_sum
    global RR_Speed
    global n
    mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if result[i] == j:
                mat[i, j] = 1
            elif (i + j) % 2 == 0:
                mat[i, j] = -1
            else:
                mat[i, j] = 0
    my_cmap = matplotlib.colors.LinearSegmentedColormap.from_list('my_camp', ['white', 'black', 'yellow'], 3)
    plt.ion()
    plt.imshow(mat, cmap=my_cmap)
    plt.title("NO." + str(answer_sum) + "answer", fontsize=16)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    plt.pause(RR_Speed)
    plt.clf()


# 创建按钮事件回调函数
class Button_handlers():
    # 开始执行N皇后问题求解
    def Start(self, event):
        set_queens(0)

    def Exit(self, event):
        plt.close()
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showwarning('Warning', 'Interrupted program operation')
        exit()

    # 设置n的大小（默认值为8）
    def set_4(self, event):
        global n
        n = 4
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set n to 4')

    def set_5(self, event):
        global n
        n = 5
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set n to 5')

    def set_6(self, event):
        global n
        n = 6
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set n to 6')

    def set_7(self, event):
        global n
        n = 7
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set n to 7')

    def set_8(self, event):
        global n
        n = 8
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set n to 8')

    def set_9(self, event):
        global n
        n = 9
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set n to 9')

    def set_10(self, event):
        global n
        n = 10
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set n to 10')

    def set_RR_low(self, event):
        global RR_Speed
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set display speed to low')
        RR_Speed = 0.6

    def set_RR_mid(self, event):
        global RR_Speed
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set display speed to mid')
        RR_Speed = 0.3

    def set_RR_high(self, event):
        global RR_Speed
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('Prompt', 'Successfully set display speed to high')
        RR_Speed = 0.1

    def get_n(self, event):
        global n

        def inputint():
            global n
            result = entry.get("1.0", "end")
            root_1 = tkinter.Tk()
            root_1.withdraw()
            tkinter.messagebox.showinfo('Prompt', 'Successfully set n to ' + result)
            n = int(result)
            window.destroy()

        global queens
        # 定义窗口
        window = tk.Tk()
        window.title('value of n')
        window.geometry('600x400')
        # 定义一个输入文本框
        var = tkinter.StringVar()  # 这即是输入框中的内容
        entry = tk.Text(window, height=1)
        # 对文本框内容进行打包
        entry.pack()
        # 将输入的字符赋值给n
        btn1 = tkinter.Button(window, text='Input', command=inputint)
        btn1.pack(side='right')
        print(n)


tkinter.messagebox.showwarning('Note', '1. Click "Enter the value of n", enter n in the dialog box, and then click the input button on the right to complete the initialization of n.'
                                       '2. Once the program starts running, it cannot be directly exited, otherwise an error result will be output')
# 创建容纳按钮的容器axes， plt.axes([0.7, 0.05, 0.1, 0.075])中的
# 列表代表容器子图所在方位，[左, 下, 宽, 高]，单位为图像长或宽的比例。
# plt.axes([0.7, 0.05, 0.1, 0.075])即子图的左边缘位于图像宽度40%位置，
# 下边缘距离图像下边缘宽度40%，子图宽度为图像宽度的10%，子图高度为图像高度的7.5%
ax_Start = plt.axes([0.4, 0.7, 0.2, 0.1])
ax_exit = plt.axes([0.4, 0.1, 0.2, 0.1])
ax_set_4 = plt.axes([0.15, 0.5, 0.09, 0.075])
ax_set_5 = plt.axes([0.25, 0.5, 0.09, 0.075])
ax_set_6 = plt.axes([0.35, 0.5, 0.09, 0.075])
ax_set_7 = plt.axes([0.45, 0.5, 0.09, 0.075])
ax_set_8 = plt.axes([0.55, 0.5, 0.09, 0.075])
ax_set_9 = plt.axes([0.65, 0.5, 0.09, 0.075])
ax_set_10 = plt.axes([0.75, 0.5, 0.09, 0.075])
ax_set_RR_low = plt.axes([0.25, 0.3, 0.13, 0.1])
ax_set_RR_mid = plt.axes([0.45, 0.3, 0.13, 0.1])
ax_set_RR_high = plt.axes([0.65, 0.3, 0.13, 0.1])
ax_get_n = plt.axes([0.7, 0.7, 0.13, 0.1])
# 实例化开始按钮，标签设置为空，防止与图片重叠
btn_Start = Button(ax_Start, 'Start')
# 利用on_clicked方法绑定事件
btn_Start.on_clicked(Button_handlers().Start)
# 实例化恢复大小按钮
btn_exit = Button(ax_exit, 'Exit')
btn_exit.on_clicked(Button_handlers().Exit)
btn_set_4 = Button(ax_set_4, 'n=4')
btn_set_4.on_clicked(Button_handlers().set_4)
btn_set_5 = Button(ax_set_5, 'n=5')
btn_set_5.on_clicked(Button_handlers().set_5)
btn_set_6 = Button(ax_set_6, 'n=6')
btn_set_6.on_clicked(Button_handlers().set_6)
btn_set_7 = Button(ax_set_7, 'n=7')
btn_set_7.on_clicked(Button_handlers().set_7)
btn_set_8 = Button(ax_set_8, 'n=8')
btn_set_8.on_clicked(Button_handlers().set_8)
btn_set_9 = Button(ax_set_9, 'n=9')
btn_set_9.on_clicked(Button_handlers().set_9)
btn_set_10 = Button(ax_set_10, 'n=10')
btn_set_10.on_clicked(Button_handlers().set_10)
btn_set_RR_low = Button(ax_set_RR_low, 'Low Speed')
btn_set_RR_low.on_clicked(Button_handlers().set_RR_low)
btn_set_RR_mid = Button(ax_set_RR_mid, 'Mid Speed')
btn_set_RR_mid.on_clicked(Button_handlers().set_RR_mid)
btn_set_RR_high = Button(ax_set_RR_high, 'High Speed')
btn_set_RR_high.on_clicked(Button_handlers().set_RR_high)
btn_get_n = Button(ax_get_n, 'Input n')
btn_get_n.on_clicked(Button_handlers().get_n)
plt.show()
answer_sum_str = str(answer_sum)
root = tkinter.Tk()
root.withdraw()
tkinter.messagebox.showinfo('Result', 'There are a total of ' + answer_sum_str + ' placement methods')
print(answer_sum)
