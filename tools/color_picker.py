import pyautogui
import time
import ctypes
import platform


def get_point_rgb_color(x, y):
    """
    基于屏幕坐标获取颜色信息
    :param x: x坐标
    :param y: y坐标
    :return: (r,g,b) 元组
    """
    if platform.system().lower() == 'windows':
        return get_windows_color(x, y)
    else:
        return get_normal_color(x, y)


def get_point_hex_color(x, y):
    """
    获取坐标的十六进制颜色坐标
    :param x: x坐标
    :param y: y坐标
    :return: 十六进制颜色值
    """
    rgb_color = get_point_rgb_color(x, y)
    return rgb2hex(rgb_color)


def get_windows_color(x, y):
    """
    读取windows下屏幕坐标的颜色，直接使用底层库读取，效率很快
    :param x: 屏幕横坐标
    :param y: 屏幕纵坐标
    :return: (r, g, b)
    """
    from ctypes import wintypes
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    # 注册user32中的GetDC参数和返回值
    user32.GetDC.restype = wintypes.HDC
    user32.GetDC.argtypes = (wintypes.HWND,)

    gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)
    # 注册GetPixel中的GetPixel参数和返回值
    gdi32.GetPixel.restype = wintypes.COLORREF
    gdi32.GetPixel.argtypes = (wintypes.HDC, ctypes.c_int, ctypes.c_int)

    hdc = user32.GetDC(None)
    win_point_color = gdi32.GetPixel(hdc, x, y)
    r = win_point_color & 0xFF
    g = win_point_color >> 8 & 0xFF
    b = win_point_color >> 16 & 0xFF
    return r, g, b


def get_normal_color(x, y):
    """
    其他系统备用方案，通过截屏读取屏幕某一点的颜色
    :param x: 屏幕横坐标
    :param y: 屏幕纵坐标
    :return: (r, g, b)
    """
    im = pyautogui.screenshot()
    rgb = im.getpixel((x, y))
    return rgb[0:3]


def rgb2hex(rgb):
    rgb = rgb[0:3]
    text = '#' + ''.join([hex(i)[-2:].replace('x', '0') for i in list(map(int, rgb))])
    return text


if __name__ == '__main__':
    start = time.time()
    for num in range(0, 1):
        color = get_point_rgb_color(0, 0)
        print(color)
    end = time.time()
    print(end - start)
