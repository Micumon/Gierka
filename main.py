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
        self.playground.bind("<KeyPress-space>", lambda x: player.action())
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
        checks = []
        if i == 0:
            checks = [body_pos[2]-2, body_pos[1], body_pos[2]+2, body_pos[3]]
        elif i == 1:
            checks = [body_pos[0], body_pos[1]-2, body_pos[2], body_pos[1]+2]
        elif i == 2:
            checks = [body_pos[0], body_pos[3]-2, body_pos[2], body_pos[3]+2]
        elif i == 3:
            checks = [body_pos[0]-2, body_pos[1], body_pos[0]+2, body_pos[3]]
        if len(self.pg.find_overlapping(checks[0], checks[1], checks[2], checks[3])) > 1:
            return False
        else:
            return True

    def action(self):
        body_pos = list(self.pg.coords(self.body))
        body_pos = [body_pos[0]-2, body_pos[1]-2, body_pos[2]+2, body_pos[3]+2]
        body_pos = tuple(body_pos)
        action_objects = self.pg.find_overlapping(body_pos[0], body_pos[1], body_pos[2], body_pos[3])
        action_objects = list(action_objects)
        action_objects.remove(1)
        print(action_objects)
        if len(action_objects) != 0:
            Char_name = find_character(action_objects)
            if Char_name:
                print("Hello " + Char_name + "!")


class Object:
    def __init__(self, pg):
        self.pg = pg


class Wall(Object):
    def __init__(self,  x1, y1, x2, y2, pg):
        super(Wall, self).__init__(pg)
        self.ID = self.pg.create_line(x1, y1, x2, y2)


class Chara(Object):
    def __init__(self, x1, y1, x2, y2, pg, name):
        super(Chara, self).__init__(pg)
        self.name = name
        self.ID = self.pg.create_oval(x1, y1, x2, y2)


def find_character(col_list):
    global characters
    tuple_of_id = characters.items()
    for col in col_list:
        for character in tuple_of_id:
            if character[1].ID == col:
                return character[0]
    return False


root = Tk()
gra = Gra(root)
player = Player("klops", gra.playground)
objects = {"wall1": Wall(50, 61, 45, 100, gra.playground)}
characters = {"Włodek": Chara(100, 100, 110, 110, gra.playground, "Włodek")}
root.mainloop()

