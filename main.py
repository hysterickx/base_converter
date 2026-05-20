# ====================
# РАЗДЕЛ 1. ВЫЗОВ МОДУЛЕЙ, СОЗДАНИЕ ОКНА ПРОГРАММЫ, КЛЮЧЕВЫЕ ПЕРЕМЕННЫЕ
# ====================

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from random import choice

ctk.set_appearance_mode ('dark')
app = ctk.CTk()
app.title ('Base converter')
app.geometry ('600x500+800+450')
app.resizable (False, False)
app.attributes ('-alpha', 0.9)
main = ctk.CTkFrame(app)
main.pack(fill = 'both', expand = True)

process = ['Считаю, подсчитываю...', 'Думаю, гадаю...', 'Генерирую процесс...', 'Нужно пару секундочек...', 'Надо посчитать...']
goodbye = ['До новых встреч!', 'Заглядывай ко мне ещё!', 'Был рад поработать с тобой!', 'Ты это, заходи, если что...', 'Надеюсь, еще увидимся!']
again = ['Возобновляю цикл...', 'Создаю всё заного...', 'Очищаю всё лишнее...', 'Отлично! Продолжаем...', 'Дай мне пару секундочек...']

# ====================
# РАЗДЕЛ 2. ФУНКЦИИ - ИСПОЛНИТЕЛИ
# ====================

def farewell():
    switch_to(page9)
    page9.after(5000, app.destroy)

def clear_all():
    def go_to_page3():
        switch_to(page8)
        page8.after(5000, lambda: switch_to(page3))

    page3.from_where.set('2')
    page4.to_where.set('10')
    page5.num.delete(0, 'end')
    go_to_page3()

def copy():
    text = page7.label2.cget('text')
    app.clipboard_clear()
    app.clipboard_append(text)
    app.update()

def switch_to(page):
    for child in main.winfo_children():
        child.pack_forget()
    page.pack(fill = 'both', expand = True)

def check_cc():
    def go_to_page5():
        switch_to(page5)
        page5.after(200, lambda: page5.num.focus_force())

    if page3.from_where.get() == page4.to_where.get():
        message = CTkMessagebox (app, width = 300, height = 150, title = 'Ошибочка', message = 'Выбраны одинаковые системы',
        icon = 'info', justify = 'center', button_color = '#ffffff', button_hover_color = '#ffcc66', button_text_color = '#000000')
    else:
        go_to_page5()

def check_num():
    from_where = page3.from_where.get()
    num = page5.num.get()
    entry = page5.num
    flag = True

    for i in num:
        if from_where == '16' and i.isalnum() == False or (i.isalpha() and i.upper() not in 'ABCDEF'):
            flag = False
            break
        elif from_where == '10' and i.isdigit() == False:
            flag = False
            break
        elif from_where == '8' and (i.isdigit() == False or int(i) > 7):
            flag = False
            break
        elif from_where == '2' and (i.isdigit() == False or int(i) > 1):
            flag = False
            break

    if len(num) == 0:
        message = CTkMessagebox (app, width = 300, height = 150, title = 'Ошибочка', message = 'Нужно ввести хоть что-то :)',
        icon = 'info', justify = 'center', button_color = '#ffffff', button_hover_color = '#ffcc66', button_text_color = '#000000')
        app.wait_window(message)
        entry.focus_force()

    elif len(num) > 25:
        message = CTkMessagebox (app, width = 300, height = 150, title = 'Ошибочка', message = 'Слишком большое число',
        icon = 'info', justify = 'center', button_color = '#ffffff', button_hover_color = '#ffcc66', button_text_color = '#000000')
        entry.delete (0, 'end')
        app.wait_window(message)
        entry.focus_force()

    elif from_where == '2' and flag == False:
        message = CTkMessagebox (app, width = 300, height = 150, title = 'Ошибочка', message = 'В двоичной системе допускаются только цифры "0" и "1"',
        icon = 'info', justify = 'center', button_color = '#ffffff', button_hover_color = '#ffcc66', button_text_color = '#000000')
        entry.delete (0, 'end')
        app.wait_window(message)
        entry.focus_force()

    elif from_where == '8' and flag == False:
        message = CTkMessagebox (app, width = 300, height = 150, title = 'Ошибочка', message = 'В восьмеричной системе допускаются только цифры от 0 до 7 включительно',
        icon = 'info', justify = 'center', button_color = '#ffffff', button_hover_color = '#ffcc66', button_text_color = '#000000')
        entry.delete (0, 'end')
        app.wait_window(message)
        entry.focus_force()

    elif from_where == '10' and flag == False:
        message = CTkMessagebox (app, width = 300, height = 150, title = 'Ошибочка', message = 'В десятичной системе допускаются только цифры',
        icon = 'info', justify = 'center', button_color = '#ffffff', button_hover_color = '#ffcc66', button_text_color = '#000000')
        entry.delete (0, 'end')
        app.wait_window(message)
        entry.focus_force()

    elif from_where == '16' and flag == False:
        message = CTkMessagebox (app, width = 300, height = 150, title = 'Ошибочка', message = 'В шестнадцатеричной системе допускаются только все цифры и буквы "ABCDEF"',
        icon = 'info', justify = 'center', button_color = '#ffffff', button_hover_color = '#ffcc66', button_text_color = '#000000')
        entry.delete (0, 'end')
        app.wait_window(message)
        entry.focus_force()

    else:
        calculate()

def calculate():
    def go_to_page7():
        switch_to(page6)
        page6.after(5000, lambda: switch_to(page7))

    from_where = page3.from_where.get()
    to_where = page4.to_where.get()
    num = page5.num.get().upper()

    num = list(num)
    result1 = 0

    for i in range(len(num)):
        if num[i] == 'A':
            num[i] = '10'
        elif num[i] == 'B':
            num[i] = '11'
        elif num[i] == 'C':
            num[i] = '12'
        elif num[i] == 'D':
            num[i] = '13'
        elif num[i] == 'E':
            num[i] = '14'
        elif num[i] == 'F':
            num[i] = '15'
    for i in range(len(num)):
        result1 += int(num[i]) * int(from_where) ** (len(num) - 1 - i)

    result2 = []
    num = result1
    to_where = int(to_where)
    while num > 0:
        result2.append(str(num % to_where))
        num //= to_where
    for i in range(len(result2)):
        if result2[i] == '10':
            result2[i] = 'A'
        elif result2[i] == '11':
            result2[i] = 'B'
        elif result2[i] == '12':
            result2[i] = 'C'
        elif result2[i] == '13':
            result2[i] = 'D'
        elif result2[i] == '14':
            result2[i] = 'E'
        elif result2[i] == '15':
            result2[i] = 'F'
    result2 = ''.join (result2[::-1])

    page6.label.configure(text = choice(process))
    page8.label.configure(text = choice(again))
    page7.label1.configure(text = page5.num.get().upper())

    if to_where == '10':
        page7.label2.configure(text = result1)
    elif from_where == '10':
        page7.label2.configure(text = result2)
    elif to_where != '10' and from_where != '10':
        page7.label2.configure(text = result2)

    go_to_page7()

# ====================
# РАЗДЕЛ 3. ФУНКЦИИ - СТРОИТЕЛИ
# ====================

def salutations(main):
    frame1 = ctk.CTkFrame(main)
    frame1.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame1, text = 'Приветствую!',
    font = ('Constantia', 27), text_color = '#ffcc66')
    label.place(relx = 0.5, rely = 0.1, anchor = 'c')

    label = ctk.CTkLabel (frame1, text = 'Эта маленькая програмка поможет тебе',
    font = ('Constantia', 27), text_color = '#ffffff')
    label.place(relx = 0.5, rely = 0.25, anchor = 'c')

    label = ctk.CTkLabel (frame1, text = 'перевести твоё число',
    font = ('Constantia', 27), text_color = '#ffcc66')
    label.place(relx = 0.5, rely = 0.4, anchor = 'c')

    label = ctk.CTkLabel (frame1, text = 'из одной системы счисления',
    font = ('Constantia', 27), text_color = '#ffffff')
    label.place(relx = 0.5, rely = 0.55, anchor = 'c')

    label = ctk.CTkLabel (frame1, text = 'в любую другую',
    font = ('Constantia', 27), text_color = '#ffcc66')
    label.place(relx = 0.5, rely = 0.7, anchor = 'c')

    button = ctk.CTkButton (frame1, width = 70, height = 50, corner_radius = 40, text = 'Отлично!', fg_color = '#FFFFFF',
    hover_color = '#ffcc66', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page2))
    button.place(relx = 0.5, rely = 0.85, anchor = 'c')

    return frame1

def rules(main):
    frame2 = ctk.CTkFrame(main)
    frame2.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame2, text = 'Систем счисления существует множество,\n но здесь используются 4 основные:',
    font = ('Constantia', 25), text_color = '#ffffff')
    label.place(relx = 0.5, rely = 0.15, anchor = 'c')

    label = ctk.CTkLabel (frame2, text = 'Двоичная: (0, 1)\nВосьмеричная: (0-7)\nДесятичная: (0-9)\nШестнадцатеричная: (0-9), (A, B, C, D, E, F)',
    font = ('Constantia', 27), text_color = '#ffcc66')
    label.place(relx = 0.5, rely = 0.4, anchor = 'c')

    label = ctk.CTkLabel (frame2, text = 'Число, которое ты вводишь, и которое получаешь\n - должны относиться к одной из этих систем',
    font = ('Constantia', 24), text_color = '#ffffff')
    label.place(relx = 0.5, rely = 0.65, anchor = 'c')

    button = ctk.CTkButton (frame2, width = 70, height = 50, corner_radius = 40, text = 'Далее', fg_color = '#FFFFFF',
    hover_color = '#ffcc66', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page3))
    button.place(relx = 0.5, rely = 0.85, anchor = 'c')

    return frame2

def from_where(main):
    frame3 = ctk.CTkFrame(main)
    frame3.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame3, text = 'Из какой системы\nпереводим число?',
    font = ('Constantia', 25), text_color = '#ffffff')
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    frame3.from_where = ctk.StringVar(value = '2')

    box = ctk.CTkRadioButton (frame3, text = '2', font = ('Calibri', 23), text_color = '#ffcc66', fg_color = '#ffcc66',
    border_color = '#ffcc66', hover_color = '#FFFFFF', border_width_unchecked = 1, variable = frame3.from_where, value = '2')
    box.place(relx = 0.25, rely = 0.5, anchor = 'c')

    box = ctk.CTkRadioButton (frame3, text = '8', font = ('Calibri', 23), text_color = '#ffcc66', fg_color = '#ffcc66',
    border_color = '#ffcc66', hover_color = '#FFFFFF', border_width_unchecked = 1, variable = frame3.from_where, value = '8')
    box.place(relx = 0.45, rely = 0.5, anchor = 'c')

    box = ctk.CTkRadioButton (frame3, text = '10', font = ('Calibri', 23), text_color = '#ffcc66', fg_color = '#ffcc66',
    border_color = '#ffcc66', hover_color = '#FFFFFF', border_width_unchecked = 1, variable = frame3.from_where, value = '10')
    box.place(relx = 0.65, rely = 0.5, anchor = 'c')

    box = ctk.CTkRadioButton (frame3, text = '16', font = ('Calibri', 23), text_color = '#ffcc66', fg_color = '#ffcc66',
    border_color = '#ffcc66', hover_color = '#FFFFFF', border_width_unchecked = 1, variable = frame3.from_where, value = '16')
    box.place(relx = 0.85, rely = 0.5, anchor = 'c')

    button = ctk.CTkButton (frame3, width = 70, height = 50, corner_radius = 40, text = 'Далее', fg_color = '#FFFFFF',
    hover_color = '#ffcc66', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page4))
    button.place(relx = 0.65, rely = 0.7, anchor = 'c')

    button = ctk.CTkButton (frame3, width = 70, height = 50, corner_radius = 40, text = 'Назад', fg_color = '#FFFFFF',
    hover_color = '#ffcc66', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page2))
    button.place(relx = 0.35, rely = 0.7, anchor = 'c')

    return frame3

def to_where(main):
    frame4 = ctk.CTkFrame(main)
    frame4.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame4, text = 'В какую систему\nпереводим число?',
    font = ('Constantia', 25), text_color = '#ffcc66')
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    frame4.to_where = ctk.StringVar(value = '10')

    box = ctk.CTkRadioButton (frame4, text = '2', font = ('Calibri', 23), text_color = '#FFFFFF', fg_color = '#FFFFFF',
    border_color = '#FFFFFF', hover_color = '#ffcc66', border_width_unchecked = 1, variable = frame4.to_where, value = '2')
    box.place(relx = 0.25, rely = 0.5, anchor = 'c')

    box = ctk.CTkRadioButton (frame4, text = '8', font = ('Calibri', 23), text_color = '#FFFFFF', fg_color = '#FFFFFF',
    border_color = '#FFFFFF', hover_color = '#ffcc66', border_width_unchecked = 1, variable = frame4.to_where, value = '8')
    box.place(relx = 0.45, rely = 0.5, anchor = 'c')

    box = ctk.CTkRadioButton (frame4, text = '10', font = ('Calibri', 23), text_color = '#FFFFFF', fg_color = '#FFFFFF',
    border_color = '#FFFFFF', hover_color = '#ffcc66', border_width_unchecked = 1, variable = frame4.to_where, value = '10')
    box.place(relx = 0.65, rely = 0.5, anchor = 'c')

    box = ctk.CTkRadioButton (frame4, text = '16', font = ('Calibri', 23), text_color = '#FFFFFF', fg_color = '#FFFFFF',
    border_color = '#FFFFFF', hover_color = '#ffcc66', border_width_unchecked = 1, variable = frame4.to_where, value = '16')
    box.place(relx = 0.85, rely = 0.5, anchor = 'c')

    button = ctk.CTkButton (frame4, width = 70, height = 50, corner_radius = 40, text = 'Далее', fg_color = '#FFFFFF',
    hover_color = '#ffcc66', text_color = '#000000', font= ('Constantia', 25), command = check_cc)
    button.place(relx = 0.65, rely = 0.7, anchor = 'c')

    button = ctk.CTkButton (frame4, width = 70, height = 50, corner_radius = 40, text = 'Назад', fg_color = '#FFFFFF',
    hover_color = '#ffcc66', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page3))
    button.place(relx = 0.35, rely = 0.7, anchor = 'c')

    return frame4

def input_number(main):
    frame5 = ctk.CTkFrame(main)
    frame5.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame5, text = 'Введи число,\n\nкоторое будем преобразовывать\n\n(не более 25 символов)',
    font = ('Constantia', 25), text_color = '#ffcc66')
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    frame5.num = ctk.CTkEntry (frame5, width = 300, height = 30, corner_radius = 40, justify = 'c', font = ('Cambria', 27))
    frame5.num.place(relx = 0.5, rely = 0.6, anchor = 'c')

    frame5.num.focus()

    button = ctk.CTkButton (frame5, width = 70, height = 50, corner_radius = 40, text = 'Далее', fg_color = '#FFFFFF',
    hover_color = '#ffcc66', text_color = '#000000', font= ('Constantia', 25), command = check_num)
    button.place(relx = 0.65, rely = 0.8, anchor = 'c')

    button = ctk.CTkButton (frame5, width = 70, height = 50, corner_radius = 40, text = 'Назад', fg_color = '#FFFFFF',
    hover_color = '#ffcc66', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page4))
    button.place(relx = 0.35, rely = 0.8, anchor = 'c')

    return frame5

def waiting(main):
    frame6 = ctk.CTkFrame(main)
    frame6.pack(fill = 'both', expand = True)

    frame6.label = ctk.CTkLabel (frame6, text = choice(process),
    font = ('Constantia', 25), text_color = '#ffffff')
    frame6.label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    return frame6

def final_page(main):
    frame7 = ctk.CTkFrame(main)
    frame7.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame7, text = 'Изначальное число:', corner_radius = 40, fg_color = '#996633', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.1, anchor = 'c')

    frame7.label1 = ctk.CTkLabel (frame7, text = '', wraplength = 550, justify = 'center', font = ('Cambria', 27))
    frame7.label1.place(relx = 0.5, rely = 0.25, anchor = 'c')

    label = ctk.CTkLabel (frame7, text = 'Результат:', corner_radius = 40, fg_color = '#996633', font = ('Constantia', 27))
    label.place(relx = 0.35, rely = 0.45, anchor = 'c')

    frame7.label2 = ctk.CTkLabel (frame7, text = '', wraplength = 550, justify = 'center', font = ('Cambria', 27))
    frame7.label2.place(relx = 0.5, rely = 0.6, anchor = 'c')

    label = ctk.CTkLabel (frame7, text = 'Хотите повторить?', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.8, anchor = 'c')

    button = ctk.CTkButton (frame7, width = 90, height = 50, corner_radius = 40, text = 'Да', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = clear_all)
    button.place(relx = 0.35, rely = 0.9, anchor = 'c')

    button = ctk.CTkButton (frame7, width = 70, height = 50, corner_radius = 40, text = 'Нет', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = farewell)
    button.place(relx = 0.65, rely = 0.9, anchor = 'c')

    button = ctk.CTkButton (frame7, corner_radius = 50, text = 'Копировать', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = copy)
    button.place(relx = 0.65, rely = 0.45, anchor = 'c')

    return frame7

def repeat(main):
    frame8 = ctk.CTkFrame(main)
    frame8.pack(fill = 'both', expand = True)

    frame8.label = ctk.CTkLabel (frame8, text = choice(again),
    font = ('Constantia', 25), text_color = '#ffffff')
    frame8.label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    return frame8

def end(main):
    frame9 = ctk.CTkFrame(main)
    frame9.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame9, text = choice(goodbye),
    font = ('Constantia', 25), text_color = '#ffffff')
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    return frame9

page1 = salutations(main)
page2 = rules(main)
page3 = from_where(main)
page4 = to_where(main)
page5 = input_number(main)
page6 = waiting(main)
page7 = final_page(main)
page8 = repeat(main)
page9 = end(main)

switch_to(page1)

app.mainloop()
