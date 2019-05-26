import time
import tkinter
import tkinter.messagebox
from threading import Thread
from random import randint


def main():

    # class download task handler 下载处理器
    class DownloadTaskHandler(Thread):
        def run(self):
            random_time = randint(0, 5)
            print('预计下载时间: %s (s) ... ' % random_time)
            time.sleep(random_time)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            # 启用下载按钮
            button_down.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button_down.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button_down = tkinter.Button(panel, text='下载', command=download)
    button_down.pack(side='left')
    button_about = tkinter.Button(panel, text='关于', command=show_about)
    button_about.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()