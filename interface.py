import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Radiobutton
import core


file = ''

text_cesar = 'Введите значение ключа: если нужно сдвинуть вправо'\
' - положительное число, влево - отрицательное'

text_vizhener = 'Введите значение ключа: слово без цифр, пробелов и строчными буквами'


def interface():
    """User interaction function """


    def fun_message():
        """The function informs the user and the type of key that

         corresponds to the selected cipher """

        tk.messagebox.showinfo('Цезарь', text_cesar) if \
            rad.get() == 'Цезарь' else tk.messagebox.showinfo('Виженер', text_vizhener)

    def message_error():
        """The function informs the user about an error """

        if core.errors_core(txt_1.get(), rad.get()) != False:
            tk.messagebox.showerror('Ошибка', 'Введено некорректное значение')
        else:
            tk.messagebox.showinfo('Оповещение', 'Файл создан')

    def cliked():
        """The function returns the path to the file in a variable"""

        global file
        file = filedialog.askopenfilename()
        return file

    def new_file():
        """The function passes values to create a file, notifies about its creation"""

        core.key_file(txt_2.get(), txt_1.get())
        tk.messagebox.showinfo('Оповещение', 'Файл создан')

    def end_fun():
        """  The function passes previously received values

        for file encryption, notifies about its creation

        """

        core.end_programm(txt_3.get(), file, txt_1.get(), rad.get())
        tk.messagebox.showinfo('Оповещение', 'Файл зашифрован')

    """Block for creating an interface window"""

    window = tk.Tk()
    window.title("Шифровальщик")
    window.geometry('600x150')

    """Block for cipher buttons"""

    lbl_1 = tk.Label(window, text="Выберите требуемый тип шифра", font=("Times New Roman", 11))
    lbl_1.grid(column=0, row=0)
    rad = tk.StringVar()
    rad1 = Radiobutton(window, text='Цезарь', value='Цезарь', variable = rad, command = fun_message)
    rad2 = Radiobutton(window, text='Виженер', value='Виженер',  variable = rad, command = fun_message)
    rad1.grid(column=1, row=0)
    rad2.grid(column=3, row=0)

    """Block for creating a key"""

    lbl_2 = tk.Label(window, text='Введите значение ключа', font=("Times New Roman", 11))
    lbl_2.grid(column=0, row=1)
    txt_1 = tk.Entry(window, width=10)
    txt_1.grid(column=1, row=1)
    btn_1 = tk.Button(window, text="Ок", command=message_error)
    btn_1.grid(column=2, row=1)
    lbl_3 = tk.Label(window, text="Введите название для файла ключа", font=("Times New Roman", 11))
    lbl_3.grid(column=0, row=2)
    txt_2 = tk.Entry(window, width=10)
    txt_2.grid(column=1, row=2)
    btn_2 = tk.Button(window, text="Ок", command=new_file)
    btn_2.grid(column=2, row=2)

    """Source text search block"""

    btn_3 = tk.Button(window, text="Выберите файл, который нужно зашифровать",
    font=("Times New Roman", 11), command = cliked)
    btn_3.grid(column=0, row=3)

    """Block for creating a file with ciphertext"""

    lbl_4 = tk.Label(window, text="Введите название для файла, в котором будет храниться\n"
    'зашифрованный текст', font=("Times New Roman", 11))
    lbl_4.grid(column=0, row=4)
    txt_3 = tk.Entry(window, width=10)
    txt_3.grid(column=1, row=4)
    btn_4 = tk.Button(window, text="Ок", command=end_fun)
    btn_4.grid(column=2, row=4)
    window.mainloop()