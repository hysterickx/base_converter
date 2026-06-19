import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
from random import choice


class StaticPages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        page_config = cfg.STATIC_PAGES_DATA[page_name]
        label_data = page_config['labels']
        button_data = page_config['buttons']

        for text, color, font, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=0.5, rely=rely, anchor='c')

        command_data = {
            'exit': controller.exit_app,
            'next': lambda: controller.switch_to('RulesPage'),
            'start': controller.create_app
        }

        for text, command_key, relx in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=command_data[command_key],
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=0.9, anchor='c')


class ChoicePages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.controller = controller
        self.page_name = page_name
        page_config = cfg.CHOICE_PAGES_DATA[page_name]
        question = page_config['question']
        box_data = page_config['boxes']
        button_data = page_config['buttons']
        default_value = page_config['default_value']
        back_page = page_config['back_page']
        self.next_page = page_config['next_page']

        label = ctk.CTkLabel(
            self,
            text=question,
            text_color=cfg.COLOR_LIME,
            font=cfg.FONT_LARGE
        )
        label.place(relx=0.5, rely=0.3, anchor='c')

        self.choice_var = ctk.StringVar(
            value=default_value
        )

        for text, value, relx in box_data:
            box = ctk.CTkRadioButton(
                self,
                text=text,
                variable=self.choice_var,
                value=value,
                **cfg.BOX_PARAMS
            )
            box.place(relx=relx, rely=0.55, anchor='c')

        command_data = {
            'back': lambda: controller.switch_to(back_page),
            'next': self.send_info
        }

        for text, command_key, relx in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=command_data[command_key],
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=0.8, anchor='c')

    def send_info(self):
        info = self.choice_var.get()
        self.controller.transfer_info(self.page_name, info)

    def get_result(self, result):
        if result in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                message=cfg.ERROR_MESSAGES[result],
                **cfg.MSG_PARAMS
            )
            return

        self.controller.switch_to(self.next_page)

    def update_ui(self, new_value):
        self.choice_var.set(new_value)


class InputPage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.controller = controller

        label_data = [
            (
                'Какое число\nнужно преобразовать?',
                cfg.COLOR_LIME, cfg.FONT_LARGE, 0.3
            ),
            (
                '(Не более 25 символов)',
                cfg.COLOR_WHITE, cfg.FONT_SMALL, 0.45
            )
        ]

        for text, color, font, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=0.5, rely=rely, anchor='c')

        self.entry = ctk.CTkEntry(
            self,
            **cfg.ENTRY_PARAMS
        )
        self.entry.place(relx=0.5, rely=0.55, anchor='c')

        button_data = [
            (
                'Назад',
                lambda: self.controller.switch_to('ToWherePage'),
                0.35
            ),
            ('Далее', self.send_info, 0.65)
        ]

        for text, command, relx in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=0.8, anchor='c')

    def get_focus(self):
        self.entry.focus()

    def send_info(self):
        info = self.entry.get()
        self.controller.transfer_info('InputPage', info)

    def get_result(self, result):
        if result in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                message=cfg.ERROR_MESSAGES[result],
                **cfg.MSG_PARAMS
            )
            self.wait_window(error_message)
            self.entry.delete(0, 'end')
            self.get_focus()
            return

        self.controller.transfer_final_info(
            self.entry.get().strip().upper(), result
        )

    def update_ui(self):
        self.entry.delete(0, 'end')


class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master,  fg_color=cfg.COLOR_DARK)
        self.controller = controller

        self.labels = {}

        label_data = [
            (
                'user_input_label',
                '',
                cfg.COLOR_WHITE,
                cfg.FONT_MEDIUM, 0.2
            ),
            (
                'result_label',
                '',
                cfg.COLOR_LIME,
                cfg.FONT_LARGE, 0.5
            ),
            (
                'again_label',
                'Хотите повторить?',
                cfg.COLOR_WHITE,
                cfg.FONT_MEDIUM, 0.8
            )
        ]

        for name, text, color, font, rely in label_data:
            label = ctk.CTkLabel(
                self,
                wraplength=500,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=0.5, rely=rely, anchor='c')
            self.labels[name] = label

        button_data = [
            (
                'Выйти',
                self.controller.exit_app,
                0.35, 0.9, cfg.BTN_PARAMS
            ),
            (
                'Давай!',
                lambda: self.controller.create_app(restart=True),
                0.65, 0.9, cfg.BTN_PARAMS
            ),
            (
                'Скопировать',
                lambda: copy(self.result),
                0.5, 0.7, cfg.COPY_BTN_PARAMS
            )
        ]

        for text, command, relx, rely, params in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **params
            )
            button.place(relx=relx, rely=rely, anchor='c')

    def get_result(self, user_input, result):
        input_label = self.labels['user_input_label']
        result_label = self.labels['result_label']
        self.result = result

        input_label.configure(text=f'Изначальное число:\n{user_input}')
        result_label.configure(text=f'Результат конвертации:\n{result}')


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        self.label = ctk.CTkLabel(
            self,
            wraplength=500,
            text='',
            text_color=cfg.COLOR_LIME,
            font=cfg.FONT_LARGE
        )
        self.label.place(
            relx=0.5,
            rely=0.5,
            anchor='c'
        )

    def change_message(self, status):
        self.label.configure(
            text=choice(cfg.ACTIVE_MESSAGES[status])
        )


class MainLogic:
    def __init__(self):
        self.main_data = {
            'from_where': '',
            'to_where': '',
            'user_input': ''
        }

    def check_input(self, page, info):
        if page == 'FromWherePage':
            self.main_data['from_where'] = info
            return 'success'

        if page == 'ToWherePage':
            if info == self.main_data['from_where']:
                return 'same_base'
            self.main_data['to_where'] = info
            return 'success'

        if page == 'InputPage':
            info = info.strip().upper()
            if not info:
                return 'empty'
            if len(info) > 25:
                return 'too_big'

            from_where = self.main_data['from_where']

            try:
                int(info, int(from_where))
            except ValueError:
                return f'wrong_{from_where}'

            self.main_data['user_input'] = info
            return self.convert_the_number()

    def convert_the_number(self):
        info = self.main_data['user_input']
        base_from = int(self.main_data['from_where'])
        base_to = int(self.main_data['to_where'])

        decimal_value = int(info, base_from)

        if base_to == 10:
            return str(decimal_value)
        elif base_to == 2:
            return bin(decimal_value)[2:]
        elif base_to == 8:
            return oct(decimal_value)[2:]
        elif base_to == 16:
            return hex(decimal_value)[2:].upper()


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Digits Converter')
        self.geometry('600x500+800+450')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.main_logic = MainLogic()
        self.is_first_load = True
        self.pages = {}
        self.current_frame = None
        page_types = [
            (cfg.STATIC_PAGES_DATA, StaticPages),
            (cfg.CHOICE_PAGES_DATA, ChoicePages),
            (None, InputPage),
            (None, MessagePage),
            (None, FinalPage)
        ]

        for config_dict, page_class in page_types:
            if config_dict is not None:
                for page_name in config_dict.keys():
                    self.pages[page_name] = page_class(
                        master=self.main_frame,
                        controller=self,
                        page_name=page_name
                    )
            else:
                page_name = page_class.__name__
                self.pages[page_name] = page_class(
                    master=self.main_frame,
                    controller=self
                )
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)
        if page_name == 'InputPage':
            self.current_frame.get_focus()

    def transfer_info(self, page, info):
        result = self.main_logic.check_input(page, info)
        self.pages[page].get_result(result)

    def transfer_final_info(self, user_input, result):
        self.pages['MessagePage'].change_message('waiting')
        self.switch_to('MessagePage')
        self.pages['FinalPage'].get_result(user_input, result)
        self.after(3000, lambda: self.switch_to('FinalPage'))

    def exit_app(self):
        self.pages['MessagePage'].change_message('farewell')
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)

    def create_app(self, restart=False):
        if restart:
            self.is_first_load = True

        if self.is_first_load:
            self.is_first_load = False
            self.pages['MessagePage'].change_message('loading')
            self.switch_to('MessagePage')
            self.pages['FromWherePage'].update_ui('10')
            self.pages['ToWherePage'].update_ui('2')
            self.pages['InputPage'].update_ui()
            self.after(3000, lambda: self.switch_to('FromWherePage'))
            return

        self.switch_to('FromWherePage')


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()