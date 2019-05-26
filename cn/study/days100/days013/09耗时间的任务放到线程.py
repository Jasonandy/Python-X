import time
import tkinter
import tkinter.messagebox


def download():
    tkinter.messagebox.showinfo('提示', '开始下载!')
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(3)
    tkinter.messagebox.showinfo('提示', '下载完成!')


def show_about():
    tkinter.messagebox.showinfo('关于', '作者: Jason(v1.0)')


def main():
    top = tkinter.Tk()
    top.title('单线程')
    label = tkinter.Label(top, text='下载器', font='Arial -32', fg='red')
    label.pack(expand=1)
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()

