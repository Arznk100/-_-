from tkinter import *
from random import randint

WIDTH = 300
HEIGHT = 200

class Ball:
    def __init__(self, *args, color = 'green'):
        self.R = randint(10, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=color)

    def move(self):
        if self.x + self.R > root.winfo_width() or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > root.winfo_height() or self.y - self.R <= 0:
            self.dy = -self.dy
        self.x += self.dx
        self.y += self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

def click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)

root = Tk()
root.geometry('300x300')
root.update()

canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=True)

new_ball = lambda *args:balls.append(Ball(color = f'#{randint(0,  0xFFFFFF):06x}'))

canvas.bind('<Button-1>',new_ball)
balls = [Ball() for i in range(5)]

tick()
root.mainloop()