from random import randint

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 2E30
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 50
    """Сила по оси **x**"""

    Fy = 50
    """Сила по оси **y**"""

    R = 10
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 6E24
    """Масса планеты"""

    x = 100
    """Координата по оси **x**"""

    y = 100
    """Координата по оси **y**"""

    Vx = 5
    """Скорость по оси **x**"""

    Vy = 5
    """Скорость по оси **y**"""

    Fx = 10
    """Сила по оси **x**"""

    Fy = 10
    """Сила по оси **y**"""

    R = 3
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = 0
    body.Fy = 0
    for obj in space_objects:
        if body != obj:
            rx = body.x - obj.x
            ry = body.y - obj.y
            r = (rx**2 + ry**2)**0.5
            F = gravitational_constant * obj.m * body.m / (r**2)
            body.Fx += -F * (rx/r)
            body.Fy += -F * (ry/r)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.Vx += ax*dt
    body.x += body.Vx*dt
    ay = body.Fy/body.m
    body.Vy += ay*dt
    body.y += body.Vy*dt
    '''zhitь ( ͡ಥ ͜ʖ ͡ಥ)'''


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")