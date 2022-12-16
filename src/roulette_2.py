import tkinter as tk


class RouletteApp():

    def __init__(self):
        # window size
        self.win_w = 800
        self.win_h = 800
        self.win_size = "{}x{}".format(self.win_w, self.win_h)
        # root
        self.root = tk.Tk()
        self.root.title("RouletteApp Part2")
        self.root.geometry(self.win_size)
        self.root.resizable(0, 0)
        # Canvas
        self.canvas = tk.Canvas(self.root,
                                width=self.win_w,
                                height=self.win_h,
                                background="#FFFFFF")
        self.canvas.place(x=0, y=0)
        # set buttons
        self.set_butttons()
        # set circle
        self.set_circle()
        self.fan_tags = ["fan01"]

    def set_butttons(self):
        print("a")# 省略

    def set_circle(self):
        # Circle Settings
        self.circle_r = 200
        circle_ltx = self.win_w / 2 - self.circle_r
        circle_lty = 200
        circle_rbx = circle_ltx + self.circle_r * 2
        circle_rby = circle_lty + self.circle_r * 2
        # Circle
        self.canvas.create_arc(circle_ltx, circle_lty, circle_rbx, circle_rby,
        width=2,
        start=30, extent=60,
        fill="#C7000B",
        tag="fan01")

    def clk_start(self):
        print("Pressed Start Button.")

    def clk_stop(self):
        print("Pressed Stop Button.")


if __name__ == '__main__':
    rouletteapp = RouletteApp()
    rouletteapp.root.mainloop()