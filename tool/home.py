import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import tkinter.simpledialog
from tkinter import *
from tool.activity import create_activity
# from .activity.create_activity import Read_activity
options=['共读活动', '锦鲤活动']




# 活动下拉选择框样式
class ttkOptionMenu(ttk.Menubutton):
    def __init__(self, master=None, **kwargs):
        values = kwargs.pop('values', [])
        command = kwargs.pop('command', None)
        textvariable = kwargs.get('textvariable')
        self.menu = kwargs.get('menu')
        if not self.menu:
            self.menu = tk.Menu()
            kwargs['menu'] = self.menu
            for v in values:
                self.menu.add_command(label=v,
                              command=tk._setit(textvariable, v, command))

        self.menu['tearoff'] = 0
        ttk.Menubutton.__init__(self, master, **kwargs)

act_type = '共读活动'
def optionCommand(value, *args):
    global act_type
    act_type = value
    # if value != '共读活动':
        # tkinter.messagebox.showinfo("警告", "暂时仅支持共读活动的创建")
        # optionVar = tk.StringVar(value='共读活动')
        # optMenu = ttkOptionMenu(top, textvariable=optionVar,
        #                         command=optionCommand, values=['共读活动', '锦鲤活动'],
        #                         direction='below')
        # optMenu.place(x=75, y=108)
    # print("这类型",act_type)
    # print('Changed:', value)


def group_switch():
    lb6.place(x=200, y=110)
    text3.place(x=260, y=113)
# 选择否则不显示输入框
def group_switch_no():
    lb6.place_forget()
    text3.place_forget()

# 调用创建活动函数
def create():
    cookie = text1.get('1.0', 'end')
    act_name = text2.get('1.0', 'end')
    if len(cookie.strip())<1:
        tkinter.messagebox.showinfo("警告", "cookie为必填项")
    elif len(act_name.strip())<1:
        tkinter.messagebox.showinfo("警告", "活动名称为必填项")
    elif act_type != "共读活动":
          tkinter.messagebox.showinfo("警告", "暂时仅支持共读活动的创建")
    else:
        act_type_num = None
        if act_type == '共读活动':
            act_type_num = 6
        cookie = cookie.strip()
        print("cookie:", cookie)
        print("活动类型：", act_type_num)
        print("活动名称：", act_name)


        a1 = create_activity.Read_activity(cookie, act_name, act_type_num)
        print("这是什么东西",a1)
        global num
        num = len(a1)
        i = 0
        str_value = ''
        while i<num:
            str1 = str(a1[i])
            str_value = str_value+"\n"+str1

            i=i+1
        # act_part_no(lb7)
        act_part(str_value)
        print(str_value)
        # act_part(a1)
        # a = create_activity.abc(cookie, act_name, act_type_num)
        # print(a)

def act_part_no(lab):
    lab.destroy()
    print("执行了吗?")

def act_part(meg):

    # lb7 = LabelFrame(top, text="进度",height=100, width=300,bg='white')
    # text4.insert(cookie)
    # text4 = Text(top, height=20, width=50)
    # lb7.place_forget()
    print("这是meg", meg)
    v3 = StringVar()
    print("v3", v3)
    # lb7 = Label(top, textvariable=v3,justify='left')
    lb7['textvariable'] = v3
    lb7['justify'] = 'left'
    v3.set(meg)
    print("这是结束的", v3)
    lb7.place(x=10, y=200)


# 关闭窗口
def click_quit():
    mess1 = tkinter.messagebox.askokcancel("提示", "是否退出？")
    if mess1 == True:
        top.quit()


if __name__ == "__main__":
    top = Tk()
    top.geometry('450x400')
    # cookie标签和输入框
    lb1 = Label(top, text="*cookie:")
    lb1.place(x=10, y=10)
    text1 = Text(top, height=1, width=20)
    text1.place(x=10, y=30)
    # 活动名称标签和输入框
    lb2 = Label(top, text="*活动名称:")
    lb2.place(x=10, y=60)
    text2 = Text(top, height=1, width=20)
    text2.place(x=10, y=80)

    lb3 = Label(top, text="活动类型:")
    lb3.place(x=10, y=110)

    lb4 = Label(top, text="是否开启团长推荐")
    lb4.place(x=200, y=10)

    lb5 = Label(top, text="是否开启小组:")
    lb5.place(x=200, y=60)

    v = StringVar()
    v.set("否")
    rad1 = tkinter.Radiobutton(top, text="是", variable=v, value="是")
    rad1.place(x=200, y=30)
    rad2 = tkinter.Radiobutton(top, text="否", variable=v, value="否")
    rad2.place(x=240, y=30)

    # 输入所需多少个小组
    lb6 = Label(top, text="小组个数:")
    text3 = Text(top, height=1, width=6)

    v2 = StringVar()
    v2.set("否")
    rad3 = tkinter.Radiobutton(top, text="是", variable=v2, value="是", command=group_switch)
    rad3.place(x=200, y=80)
    rad4 = tkinter.Radiobutton(top, text="否", variable=v2, value="否", command=group_switch_no)
    rad4.place(x=240, y=80)


    main_menu = Menu(top)
    filemenu = Menu(main_menu, tearoff=False)
    filemenu.add_command(label="测试")
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=click_quit)
    main_menu.add_cascade(label="文件", menu=filemenu)


    optionVar = tk.StringVar(value='共读活动')
    optMenu = ttkOptionMenu(top, textvariable=optionVar,
                            command=optionCommand, values=['共读活动', '锦鲤活动'],
                            direction='below')
    optMenu.place(x=75, y=108)

    # text4 = Text(top, height=20, width=50)
    lb7 = Label(top)
    # lb7.place(x=10, y=200)


    but1 = Button(top, text="一键创建活动", bg="#3582FB", fg="#ffffff", command=create)
    but1.place(x=110, y=150)

    top.config(menu=main_menu)
    top.mainloop()

