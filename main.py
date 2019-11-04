import tkinter as Tk
import os, subprocess



class ContrastApp:
    def __init__(self):
        """Constructor"""

        self.root = Tk.Tk()
        self.root.bind('<Escape>', lambda e: self.root.quit())
        # self.root.protocol("WM_DELETE_WINDOW", self.onclick_close_icon)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        print(screen_height, screen_width)
        width = 300
        height = 280
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)
        self.root.title("Moil LAB")
        self.config_file = os.path.expanduser('~') + "/.config/pyddc"

        self.c = 80
        self.d = 5

        self.g = .8
        self.h = .1

        self.screens = []

        try:
            with open(self.config_file, "r") as f:
                self.c, self.g = [float(a) for a in f.readline().split()]
        except:
            print("No config file found.")
        #####################################################################################################
        self.frame_welcome = Tk.Frame(self.root)
        self.frame_blank = Tk.Frame(self.root)
        self.frame_f1 = Tk.Frame(self.root)
        self.frame_blank1 = Tk.Frame(self.root)
        self.frame_f2 = Tk.Frame(self.root)
        self.frame_blank2 = Tk.Frame(self.root)
        self.frame_ok = Tk.Frame(self.root)

        self.frame_welcome.pack()
        self.frame_blank.pack(pady=5)
        self.frame_f1.pack(pady=5)
        self.frame_blank1.pack(pady=10)
        self.frame_f2.pack(pady=5)
        self.frame_blank2.pack()
        self.frame_ok.pack()
        self.display = Tk.StringVar()
        #####################################################################################################
        self.lab_welcome = Tk.Label(self.frame_welcome,
                                    text='Brightness app',
                                    bg="green",
                                    fg="black",
                                    width="600",
                                    height="1",
                                    font=("calibri", 14, "bold"))
        self.lab_welcome.pack()

        #####################################################################################################
        list_display = ['display-1', 'display-2', 'display-3', 'display-4', 'display-5']
        self.drop_list_courses = Tk.OptionMenu(self.frame_blank, self.display, *list_display)
        self.drop_list_courses.config(width=15, height=1, font=("verdana", 12))
        self.display.set('Select Your displays')
        self.drop_list_courses.pack()

        self.label = Tk.Label(self.frame_f1,
                                     text='Brightness',
                                     font=("calibri", 13, "bold"))
        self.label.grid(row=0, column=0, padx=10)

        self.btn_minus = Tk.Button(self.frame_blank1,
                                    text="    -    ",
                                    command=self.mb)
        self.btn_minus.grid(row=0, column=0, padx=10)

        self.btn_plus = Tk.Button(self.frame_blank1,
                                    text="    +    ",
                                    command=self.pb)
        self.btn_plus.grid(row=0, column=1, padx=10)

        self.l = Tk.Label(self.frame_blank1, text=' = ')
        self.l.grid(row=0, column=2, padx=10)

        self.lab = Tk.Label(self.frame_blank1, text='')
        self.lab.grid(row=0, column=3, padx=10)

        self.labele = Tk.Label(self.frame_f2,
                            text='Contrast',
                            font=("calibri", 13, "bold"))
        self.labele.grid(row=0, column=0, padx=10)

        self.btn_minus = Tk.Button(self.frame_blank2,
                                    text="    -    ",
                                    command=self.mg)
        self.btn_minus.grid(row=0, column=0, padx=10)

        self.btn_plus = Tk.Button(self.frame_blank2,
                                    text="    +    ",
                                    command=self.pg)
        self.btn_plus.grid(row=0, column=1, padx=10)

        self.l2 = Tk.Label(self.frame_blank2, text=' = ')
        self.l2.grid(row=0, column=2, padx=10)

        self.labg = Tk.Label(self.frame_blank2, text='')
        self.labg.grid(row=0, column=3, padx=10)

        # self.btn_attend = Tk.Button(self.frame_ok,
        #                             text="Apply",
        #                             command=self.doit)
        # self.btn_attend.pack(pady=30)

        self.setbg()
        self.get_screens()
        self.root.mainloop()

        #####################################################################################################

    def get_screens(self):
        cmd = 'xrandr -q'
        r = subprocess.check_output(cmd.split()).decode("utf-8")
        for x in r.splitlines():
            if " connected" in x:
                self.screens.append(x.split(' ')[0])
                a = x[-13:]
                print(a)

    def setbg(self):
        # print("%u%%" % self.c)
        # print("%u%%" % self.g)
        self.lab.config(text="%u%%" % self.c)
        self.labg.config(text="%.1f" % self.g)
        for scr in self.screens:
            os.system("xrandr --output %s --brightness %f --gamma %f:%f:%f" % (
                scr, self.c / 100, self.g, self.g, self.g))
        with open(self.config_file, "w") as f:
            f.write("%u %.1f" % (self.c, self.g))

    # def doit(self):
    #     os.system("ddcutil setvcp 10 %u" % self.c)
    #     os.system("ddcutil setvcp 12 %u" % self.g)
    #     with open(self.config_file, "w") as f:
    #         f.write("%u %u" % (self.c, self.g))

    def mb(self):
        global c

        if self.c > self.d:
            self.c -= self.d
        self.setbg()

    def pb(self):
        global c

        if self.c < 200 - self.d / 2:
            self.c += self.d
        self.setbg()

    def mg(self):

        global g

        if self.g > 1.5 * self.h:
            self.g -= self.h
        self.setbg()

    def pg(self):
        global g

        if self.g < 3 - self.h / 2:
            self.g += self.h
        self.setbg()


def main():
    app = ContrastApp()


if __name__ == "__main__":
    main()