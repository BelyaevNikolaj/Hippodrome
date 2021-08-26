from tkinter import *

#**************************************
# ОТСЮДА БУДЕМ ПИСПТЬ МЕЬОДЫ И ФУНКЦИИ
#**************************************

# Добавление строки в текстовый блок
def insertText(s):
    textDiary.insert(INSERT, s + '\n')
    textDiary.see(END)
    
# Расположение лошадей на экране
def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)
  
# Главное окно проги=======
root = Tk()

#**************************************
# ОТСЮДА ОПРЕДЕЛИМ ЗНАЧЕНИЯ ПЕРЕМЕННЫХ
#**************************************

#Размер окна программы
WIDTH = 1024
HEIGHT = 600

# Позиции лошадей
x01 = 20 # Устанавливаем координату х для лошади 1
x02 = 20
x03 = 20
x04 = 20

#*************************************************
# ОТСЮДА ОРГАНИЗУЕМ ФОРМИРОВАНИЕ ЭЛЕМНЕТОВ В ОКНЕ
#*************************************************

# Создаем главное окно
#Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Установка заголовка
root.title('ИППОДРОМ')

# Запрещаем изменение размера
root.resizable(False, False)

# Устанавливаем ширину, высоту и позицию
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

road_image = PhotoImage(file='road.png') # Загружаем изображение фона
road = Label(root, image=road_image) # устанавливаем изображение в Label
road.place(x=0, y=17) # Выводим изображенеи в окно

horse01_image = PhotoImage(file='horse01.png') # Загружаем изображение
horse01 = Label(root, image=horse01_image) # Устанавливаем в Label

horse02_image = PhotoImage(file='horse02.png')
horse02 = Label(root, image=horse02_image)

horse03_image = PhotoImage(file='horse03.png')
horse03 = Label(root, image=horse03_image)

horse04_image = PhotoImage(file='horse04.png')
horse04 = Label(root, image=horse04_image)

horsePlaceInWindow()

# Создаем кнопку и выводим ее на экран
startButton = Button(text='СТАРТ', font='arial 20', width=61, background = '#37AA37')
startButton.place(x=20, y=370)

textDiary = Text(width=70, height = 8, wrap=WORD)
textDiary.place(x=430, y=450)

scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary['yscrollcommand'] = scroll.set



root.mainloop()


