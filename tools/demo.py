import os
from time import sleep
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from PIL import ImageGrab, Image, ImageTk
import color_picker

root = tkinter.Tk()
root.geometry('100x40+400+300')
root.resizable(False, False)


class MyCapture:

    def __init__(self, png):
        # 变量X和Y用来记录鼠标左键按下的位置
        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)
        # 获取屏幕尺寸
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        # 创建顶级组件容器，与屏幕尺寸一样大
        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
        # 不显示最大化、最小化按钮
        self.top.overrideredirect(True)
        self.image = ImageTk.PhotoImage(file="/Users/rain/work_space/python_space/game_helper/tools/temp.png")
        # 创建画布
        self.canvas = tkinter.Canvas(self.top, bg='white', width=screenWidth, height=screenHeight)
        # 显示全屏截图，在全屏截图上进行区域截图
        self.canvas.create_image(screenWidth // 2, screenHeight // 2, image=self.image)

        # 获取鼠标左键抬起的位置，取色
        def onLeftButtonUp(event):
            # color_picker.get_point_hex_color(event.x, event.y)
            im = Image.open(png)
            color = im.getpixel((event.x, event.y))[:3]
            color = map(lambda x: hex(x)[2:], color)
            color = map(lambda x: x if len(x) == 2 else '0' + x, color)
            color = '#' + ''.join(color)
            tkinter.messagebox.showinfo('', str(color))
            # 关闭当前窗口
            self.top.destroy()
            
        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)


# 开始截图

def buttonCaptureClick():
    # 最小化主窗口
    root.state('icon')
    sleep(0.2)
    filename = 'temp.png'
    im = ImageGrab.grab()
    im.save(filename)
    im.close()
    # 显示全屏幕截图
    w = MyCapture(filename)
    buttonCapture.wait_window(w.top)
    # 截图结束，恢复主窗口，并删除临时的全屏幕截图文件
    root.state('normal')
    os.remove(filename)


buttonCapture = tkinter.Button(root, text='取色', command=buttonCaptureClick)

buttonCapture.place(x=10, y=10, width=80, height=20)

# 启动消息主循环

if __name__ == '__main__':
    root.mainloop()
