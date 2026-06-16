import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
from random import choice


class StaticPages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

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


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Digits Converter')
        self.geometry('600x500+800+450')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.is_first_load = True
        self.pages = {}
        self.current_frame = None
        page_types = [
            (cfg.STATIC_PAGES_DATA, StaticPages),
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

    def exit_app(self):
        self.pages['MessagePage'].change_message('farewell')
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)

    def create_app(self, restart=False):
        if restart:
            self.is_first_load = True

        if self.is_first_load:
            self.pages['MessagePage'].change_message('loading')
            self.switch_to('MessagePage')
            self.is_first_load = False


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()