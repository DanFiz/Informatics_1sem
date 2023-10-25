import pandas as pd
films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])
film_genres_list2 = list(films['Genre'])
# попробуйте посмотреть промежуточный результат в film_list

complex_genres = [] # будем хранить составные жанры, чтобы потом их удалить
for film_genre in film_genres_list:
    genres = film_genre.split(' | ') # разберем каждый составной жанр на составляющие
    if len(genres) > 1: # если попался составной жанр
        for genre in genres: # то пройдемся по всем элементарным жанрам фильма
            film_genres_list.append(genre) # и добавим их
        complex_genres.append(film_genre)
# обратите внимание, что мы не можем в процессе итерации через for удалять элементы, поскольку это собьет итератор. Можете посмотреть, к чему это приведет, написав вместо complex_genres.append(film_genre) сразу film_genres_list.remove(film_genre)

for genre in complex_genres:
    film_genres_list.remove(genre) # удалим все составные жанры из списка жанров

genres_set = set(film_genres_list) # чтобы сделать из этого set! теперь здесь лежат все уникальные элементарные жанры
print(genres_set)


titles = list(films['Title'])
from tkinter import *
from tkinter import ttk
from random import randrange


# Задаем функцию пересчета. обратите внимание, что к feet и meters мы обращаемся как к глобальным переменным, в общем случае так делать нехорошо
# *args означает, что функция может принимать любое количество переменных. здесь они не используется, поэтому для общности написали так
def calculate(*args):
    try:
        Genre0 = Genre.get()  # используем геттер для объекта StringVal

        index=[]
        for i in range(len(film_genres_list2)):
            if film_genres_list2[i] == Genre0:
                index.append(i)
            else:
                genres = film_genres_list2[i].split(' | ')
                for genre in genres:
                    if genre == Genre0:
                        index.append(i)
        r=randrange(len(index))
        Film.set(titles[index[r]])
    except ValueError:
        pass


# Создадим основное окно приложения
root = Tk()
root.title("Filmography")

'''
Зададим виджет Frame с названием mainframe, который будет содержать элементы нашего интерфейса.
После того, как мы создали его, grid() помещает его в окно приложения. 
columnconfigure/rowconfigure говорит что mainframe должен также расширяться
и занимать все свободное место при изменении размеров окна
'''
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

'''
Первый виджет Entry должен принимать количество футов.

Когда мы создаем виджет, нам нужно указать его родителя.
Это виджет, внутри которого будет размещен новый виджет.
Наша запись и другие виджеты, которые мы вскоре создадим, считаются дочерними элементами mainframe.
Родительский элемент передается в качестве первого параметра при создании экземпляра объекта виджета.

Также мы задали, что наше окно ввода должно иметь ширину под 7 символов.

Также мы создали глобальную переменную feet как textvariable для Entry. Туда будет сохраняться ввод в поле ввода feet_entry.
Когда ввод поменяется, Tkinter автоматически обновит feet. 
Для задания feet используется конструктор по умолчанию для таких переменных -- StringVar()

Tkinter должен знать куда вы хотите поместить виджеты относительно друг друга. 
За это отвечает функция grid. Она помещает содержимое в column (1, 2, or 3) и row (also 1, 2, or 3) окна.
sticky отвечает за то, по какой стороне будет выравнивание. W (west) означает запад, то есть левую сторону ячейки
W,E (west-east) означает и левую и правую сторону одновременно, то есть выравнивание посередине.
В Python определены константы для направлений компаса, поэтому вы можете писать просто W или (W, E).
'''
Genre = StringVar()
Genre_entry = ttk.Entry(mainframe, width=10, textvariable=Genre)
Genre_entry.grid(column=2, row=1, sticky=(W, E))

'''
Дальше создаем окно вывода. 
'''
Film = StringVar()
ttk.Label(mainframe, textvariable=Film).grid(column=2, row=2, sticky=(W, E))

'''
По нажатии на кнопку будем выполнять функцию calculate. Поскольку в ней уже прописаны операции напрямую с feet и meters,
то нам не нужно задавать какие-либо аргументы, функция автоматически положит нужное значение в meters и значение в 
определенном выше Label обновится.
'''
ttk.Button(mainframe, text="Discover", command=calculate).grid(column=3, row=3, sticky=W)

# косметические подписи, обратите внимание на расположение
ttk.Label(mainframe, text="Genre").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Is respond to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Film").grid(column=3, row=2, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# сразу помещает курсор ввода в поле feet_entry
Genre_entry.focus()
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось calculate
root.bind("<Return>", calculate)

# циклим наше окно
root.mainloop()