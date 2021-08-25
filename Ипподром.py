from tkinter import *

# Главное окно проги=======
root = Tk()

#Размер окна программы
WIDTH = 640
HEIGHT = 480

#Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Устанавливаем ширину, высоту и позицию
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# Установка заголовка
root.title('Test window')

# Запрещаем изменение размера
root.resizable(False, False)


# Кнопка 01========================

button01 = Button()

# Указываем текст на кнопке
button01['text'] = 'Button 1'

# Получаем ширину кнопки
X_BTN = WIDTH // 2 - button01.winfo_reqwidth() // 2
Y_BTN = HEIGHT // 2 - button01.winfo_reqheight() // 2
button01.place(x = X_BTN, y = Y_BTN)

root.mainloop()


