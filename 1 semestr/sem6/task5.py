from random import randint
from tkinter import *
from tkinter import ttk
WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self, random=False, event=None):
        self.R = randint(10, 50)
        nx = randint(0, 1)
        ny = randint(0, 1)
        if nx == 0:
            self.dx = 10
        else:
            self.dx = -10
        if ny == 0:
            self.dy = 10
        else:
            self.dy = -10
        if random == True:
            self.x = event.x
            self.y = event.y
            def color():
                x=hex(randint(0,255))[2:]
                if len(x)==1:
                    x='0'+x
                return x
            AA=color()
            BB=color()
            CC=color()
            color='#'+AA+BB+CC
            self.ball_id = canvas.create_oval(self.x - self.R,
                                              self.y - self.R,
                                              self.x + self.R,
                                              self.y + self.R, fill=color)
        else:
            self.x = randint(self.R, WIDTH - self.R)
            self.y = randint(self.R, HEIGHT - self.R)
            self.ball_id = canvas.create_oval(self.x - self.R,
                                        self.y - self.R,
                                        self.x + self.R,
                                        self.y + self.R, fill="green")

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0: # отражение от стенок
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0: # отр
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)
    balls.append(Ball(random=True, event=event))

#здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
#сделаем так, чтобы нажатие левой кнопки на поле выводило координаты точки, в которую мы нажали

balls = [Ball() for i in range(5)]
canvas.bind('<Button-1>', click_handler)
# делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
tick()
root.mainloop()