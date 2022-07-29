import time

import pyautogui
import color_picker

import tkinter as tk
import threading


class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.listen_click_flag = False

        self.t = threading.Thread(target=self.listen_click)
        self.t.start()

        self.pack()
        self.button = tk.Button(text="开始")
        self.button.bind("<Button-1>", self.start_click)
        self.button.pack()
        self.button = tk.Button(text="结束")
        self.button.bind("<Button-1>", self.end_click)
        self.button.pack()

    def start_click(self, event):
        self.listen_click_flag = True

    def end_click(self, event):
        self.listen_click_flag = False

    def listen_click(self):
        while True:
            time.sleep(1)
            if self.listen_click_flag:
                print("aaa")


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("400x300+200+300")
    root.title("屏幕信息助手")
    myapp = App(root)
    myapp.mainloop()
    root.mainloop()
