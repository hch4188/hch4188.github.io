import tkinter as tk
import random
import threading
import time
import math

def generate_heart_point(num_points=200):
    points = []
    for i in range(num_points):
        t = (i / num_points) * 2 * math.pi
        x = 16 * (math.sin(t) ** 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        points.append((x, y))
    return points

def show_warm_tip(x, y, screen_width, screen_height):
    window = tk.Tk()

    window_width = 200
    window_height = 50
    scale = min(screen_width, screen_height) / 40

    pos_x = int(screen_width / 2 + x * scale - window_width / 2)
    pos_y = int(screen_height / 2 + y * scale - window_height / 2)
    pos_x = max(0, min(pos_x, screen_width - window_width))
    pos_y = max(0, min(pos_y, screen_height - window_height))

    window.title('x')
    window.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

    tips = [
        "前程似锦", "万事如意", "天天开心",
        "好运常伴", "平安喜乐", "未来可期",
        "幸福满满", "勇敢追梦", "不负韶华",
        "永不言弃", "乘风破浪", "砥砺前行"
        "笑口常开"
    ]
    bg_color = [
        'lightpink', 'mistyrose', 'lavenderblush', 'pink', 'hotpink',
        'salmon', 'plum', 'violet', 'orchid', 'thistle',
    ]

    tip = random.choice(tips)
    bg = random.choice(bg_color)

    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('Microsoft YaHei', 11),
        width=25,
        height=2,
    ).pack()

    window.attributes('-topmost', True)
    try:
        window.overrideredirect(False)
    except:
        pass

    window.mainloop()

def main():
    temp_window = tk.Tk()
    screen_width = temp_window.winfo_screenwidth()
    screen_height = temp_window.winfo_screenheight()
    temp_window.destroy()

    heart_points = generate_heart_point(200)

    threads = []
    for i, (x, y) in enumerate(heart_points):
        t = threading.Thread(target=show_warm_tip, args=(x, y, screen_width, screen_height))
        threads.append(t)
        t.start()
        time.sleep(0.08)

if __name__ == '__main__':
    main()