from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint
#**************************************
# ОТСЮДА БУДЕМ ПИСПТЬ МЕЬОДЫ И ФУНКЦИИ
#**************************************

# Движение лошадей
def moveHorse():
    global x01, x02, x03, x04

    speed01 = randint(3, 10) / 10
    speed02 = randint(3, 10) / 10
    speed03 = randint(3, 10) / 10
    speed04 = randint(3, 10) / 10

    x01 += (speed01 * randint(1, (7 - state01))) / state01
    x02 += (speed02 * randint(1, (7 - state02))) / state02
    x03 += (speed03 * randint(1, (7 - state03))) / state03
    x04 += (speed04 * randint(1, (7 - state04))) / state04

    horsePlaceInWindow()
    
    if (x01 < 952 and
        x02 < 952 and
        x03 < 952 and
        x04 < 952):
        root.after(5, moveHorse)

# При нажатии на кнопку СТАРТ
def runHorse():
    global  money
    startButton['state'] = 'disabled'
    stavka01['state'] = 'disabled'
    stavka02['state'] = 'disabled'
    stavka03['state'] = 'disabled'
    stavka04['state'] = 'disabled'
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    moveHorse()
  
# Вызываем каждый раз при выборе любого Combobox
def refreshCombo(eventObject):
    summ =summ01.get() +  summ02.get() + summ03.get() + summ04.get()
    labelAllMoney['text'] = f'У Вас на счету: {int(money - summ)} {valuta}.'
        
    stavka01['values'] = getValues(int(money - summ02.get() - summ03.get() -  summ04.get()))
    stavka02['values'] = getValues(int(money - summ01.get() - summ03.get() -  summ04.get()))
    stavka03['values'] = getValues(int(money - summ02.get() - summ01.get() -  summ04.get()))
    stavka04['values'] = getValues(int(money - summ02.get() - summ03.get() -  summ01.get()))

    # Выключаем или включаем кнопку СТАРТ
    if (summ > 0):
        startButton['state'] = 'normal'
    else:
        startButton['state'] = 'disabled'
        
    if (summ01.get() > 0):
        horse01Game.set(True)
    else:
        horse01Game.set(False)

    if (summ02.get() > 0):
        horse02Game.set(True)
    else:
        horse02Game.set(False)

    if (summ03.get() > 0):
        horse03Game.set(True)
    else:
        horse03Game.set(False)

    if (summ04.get() > 0):
        horse04Game.set(True)
    else:
        horse04Game.set(False)

# Список значений для Combobox
def getValues(summa):
    value = []
    if (summa > 9):
        for i in range(0, 11):
            value.append(i * (int(summa) // 10))
    else:
        value.append(0)
        if (summa > 0):
            value.append(summa)
            
    return value

# Чтение из файла оставшейся суммы
def loadMoney():
    try:
        f = open('money.dat', 'r')
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f'Файл не существует, задано значение {defaultMoney} {valuta}')
        m = defaultMoney
    return m

# Запись суммы вфайл
def  saveMoney(moneyToSave):
    try:
        f = open('money.dat', 'w')
        f.write(str(moneyToSave))
        f.close()
    except:
        print('Ошибка содания файла, наш Ипподром закрывается!')
        quit(0)

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
    
root = Tk()


#**************************************
# ОТСЮДА ОПРЕДЕЛИМ ЗНАЧЕНИЯ ПЕРЕМЕННЫХ
#**************************************

# Финансовые показатели
valuta = 'руб.'
defaultMoney = 10000
money = 0

# Погода
weather = randint(1, 5)

# Время суток
timeDay = randint(1, 4)

#Размер окна программы
WIDTH = 1024
HEIGHT = 600

# Позиции лошадей
x01 = 20 # Устанавливаем координату х для лошади 1
x02 = 20
x03 = 20
x04 = 20

# Клички лошадей
nameHorse01 = 'Pineapple'
nameHorse02 = 'Stalker'
nameHorse03 = 'Voracious'
nameHorse04 = 'Hoof'

#*************************************************
# ОТСЮДА ОРГАНИЗУЕМ ФОРМИРОВАНИЕ ЭЛЕМНЕТОВ В ОКНЕ
#*************************************************

# Создаем главное окно
# Вычисляем координаты для размещения окна по центру
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

# Создаем вывод их на экран
horsePlaceInWindow()

# Создаем кнопку и выводим ее на экран
startButton = Button(text='СТАРТ', font='arial 20', width=61, background = '#37AA37')
startButton.place(x=20, y=370)

startButton['state'] = 'disabled'

# Создаемм имформационный чат виджетом Text
textDiary = Text(width=70, height = 8, wrap=WORD)
textDiary.place(x=430, y=450)

# Создаем и прекрепляем к тексту полосупрокрутки
scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary['yscrollcommand'] = scroll.set

# Загружаем сумму средств игрока из файла
money = loadMoney()

# Если игрок беден и несчастен, выгоняем его
if (money <= 0):
    messagebox.showinfo('Стоп!', 'На ипподроме без средств захоить нельзя!')
    quit(0)

# Формируе текстовую структуру и выводим в нее оставшуюся сумму средств
labelAllMoney = Label(text=f'Осталось средств: {money} {valuta}.', font='Arial 12')
labelAllMoney.place(x=20, y=565)

# Выводим текстовые метки  в левом нижнем углу окна
labelHorse01 = Label(text='Ставка на лошадь №1')
labelHorse01.place(x=20, y=450)

labelHorst02 = Label(text='Ставка на лошадь №2')
labelHorst02.place(x=20, y=480)

labelHorse03 = Label(text='Ставка на лошадь №3')
labelHorse03.place(x=20, y=510)

labelHorse04 = Label(text='Cтавка на лошадь №4')
labelHorse04.place(x=20, y=540)

#Checkboxes for horses
horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150,y=478)

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04,variable=horse04Game, onvalue=1,  offvalue=0)
horseCheck04.place(x=150, y=538)

# Запрещаем играку изменять значения чекбоксов
horseCheck01['state'] = 'disabled'
horseCheck02['state'] = 'disabled'
horseCheck03['state'] = 'disabled'
horseCheck04['state'] = 'disabled'

# Выпадающий список
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

# Задаем атрибут "только чтение"
stavka01['state'] = 'reabonly'
stavka01.place(x=280, y=450)

stavka02['state'] = 'reabonly'
stavka02.place(x=280, y=480)

stavka03['state']='reabonly'
stavka03.place(x=280,  y=510)

stavka04['state'] ='reabonly'
stavka04.place(x=280, y=540)

# Определяем переменные для хранения начения из Combobox
summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

# Привязываем переменные к Combobox
# В них будут хранится выбранное в виджате значение
stavka01['textvariable'] = summ01
stavka02['textvariable'] = summ02
stavka03['textvariable'] = summ03
stavka04['textvariable'] = summ04

stavka01.bind('<<ComboboxSelected>>', refreshCombo)
stavka02.bind('<<ComboboxSelected>>', refreshCombo)
stavka03.bind('<<ComboboxSelected>>', refreshCombo)
stavka04.bind('<<ComboboxSelected>>', refreshCombo)

# Обновляем значение Combox
refreshCombo('')

# Устанавливаем самое первое значение списка
stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

# УДАЛИТЬ
stavka01.current(1)
refreshCombo('')
startButton['command'] = runHorse

# Состояние лошадей 1 - великолепно! 5 - ужасно больная.
state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

#Output of the main window
root.mainloop()


