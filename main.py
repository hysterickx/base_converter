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
            label.place(
                relx=0.5,
                rely=rely,
                anchor='c'
            )

        command_data = {
            'exit': controller.exit_app,
            'rules': lambda: controller.switch_to('RulesPage'),
            'start': controller.create_app
        }

        for text, command_key, relx in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=command_data[command_key],
                **cfg.BTN_PARAMS
            )
            button.place(
                relx=relx,
                rely=0.9,
                anchor='c'
            )


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
            'rules': lambda: controller.switch_to(back_page),
            'to_where': self.send_info,
            'from_where': lambda: controller.switch_to(back_page),
            'user_input': self.send_info
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

    def get_status(self, status):
        if status in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                message=cfg.ERROR_MESSAGES[status],
                **cfg.MSG_PARAMS
            )
            return

        self.controller.switch_to(self.next_page)


class InputPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.controller = controller

        label_data = [
            (
                'Какое число\nнужно преобразовать?',
                cfg.COLOR_LIME, cfg.FONT_LARGE, 0.3
            ),
            (
                'Не более 25 символов',
                cfg.COLOR_WHITE, cfg.FONT_SMALL, 0.4
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

        entry = ctk.CTkEntry(
            self,
            **cfg.ENTRY_PARAMS
        )
        entry.place(relx=0.5, rely=0.55, anchor='c')

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

    def send_info(self):
        print('sss')


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        self.label = ctk.CTkLabel(
            self,
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
            (None, MessagePage)
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

    def transfer_info(self, page, info):
        status = self.main_logic.check_input(page, info)
        self.pages[page].get_status(status)

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
            self.after(3000, lambda: self.switch_to('FromWherePage'))
            return

        self.switch_to('FromWherePage')


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()