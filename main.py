from tkinter import *
from tkinter import ttk


class Gra:
    def __init__(self, root):
        root.title("Gra")

        mframe = ttk.Frame(root, padding=10, width=400, height=400)
        mframe.grid(column=0, row=0, sticky=(W, S, E, N))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.playground = Canvas(mframe)
        self.playground.focus_set()
        self.playground.bind("<KeyPress-Right>", lambda x: player.move(2, 0, 0))
        self.playground.bind("<KeyPress-Up>", lambda x: player.move(0, -2, 1))
        self.playground.bind("<KeyPress-Down>", lambda x: player.move(0, 2, 2))
        self.playground.bind("<KeyPress-Left>", lambda x: player.move(-2, 0, 3))
        self.playground.grid(column=1, row=1, sticky=(W, S, E, N))


class Player:
    def __init__(self, name, pg):
        self.name = name
        self.center = [55, 55]
        self.radius = 5
        self.pg = pg
        self.body = self.pg.create_oval(50, 50, 60, 60)

    def move(self, dx, dy, i):
        if self.colision_check(i):
            self.pg.move(self.body, dx, dy)

    def colision_check(self, i):
        body_pos = self.pg.coords(self.body)
        print(body_pos)
        checks = []
        if i == 0:
            checks = [body_pos[2]-2, body_pos[1], body_pos[2]+2, body_pos[3]]
        elif i == 1:
            checks = [body_pos[0], body_pos[1]-2, body_pos[2], body_pos[2]+2]
        elif i == 2:
            checks = [body_pos[0], body_pos[3]-2, body_pos[2], body_pos[3]+2]
        elif i == 3:
            checks = [body_pos[0]-2, body_pos[1], body_pos[0]+2, body_pos[3]]
        print(checks)
        print(self.pg.find_overlapping(checks[0], checks[1], checks[2], checks[3]))

        if len(self.pg.find_overlapping(checks[0], checks[1], checks[2], checks[3])) > 1:
            return False
        else:
            return True


class Object:
    def __init__(self,  x1, y1, x2, y2, pg):
        self.pg = pg
        self.pg.create_line(x1, y1, x2, y2)


root = Tk()
gra = Gra(root)
player = Player("klops", gra.playground)
objects = {"wall1": Object(50, 61, 45, 100, gra.playground)}
root.mainloop()

