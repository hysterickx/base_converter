COLOR_DARK = '#0d0a0c'
COLOR_LIME = '#99ff66'
COLOR_BLACK = '#000000'
COLOR_WHITE = '#ffffff'

FONT_LARGE = ('Constantia', 30)
FONT_MEDIUM = ('Constantia', 25)
FONT_SMALL = ('Constantia', 20)

BOX_PARAMS = {
    "font": FONT_MEDIUM,
    "text_color": COLOR_WHITE,
    "fg_color": COLOR_LIME,
    "border_color": COLOR_WHITE,
    "hover_color": COLOR_LIME,
    "border_width_checked": 5,
    "border_width_unchecked": 1
}

ENTRY_PARAMS = {
    "width": 100,
    "height": 30,
    "border_width": 0,
    "corner_radius": 40,
    "justify": 'c',
    "font": FONT_LARGE
}

MSG_PARAMS = {
    "width": 300,
    "height": 150,
    "title": 'Ошибочка',
    "icon": 'info',
    "justify": 'center',
    "button_color": COLOR_WHITE,
    "button_hover_color": COLOR_LIME,
    "button_text_color": COLOR_BLACK
}

BTN_PARAMS = {
    "width": 70,
    "height": 50,
    "corner_radius": 50,
    "fg_color": COLOR_LIME,
    "hover_color": COLOR_WHITE,
    "text_color": COLOR_BLACK,
    "font": FONT_SMALL
}

STATIC_PAGES_DATA = {
    'GreetingsPage': {
        'labels': [
            ('Приветствую!', COLOR_LIME, FONT_LARGE, 0.15),
            ('Эта маленькая програмка', COLOR_WHITE, FONT_LARGE, 0.3),
            ('поможет тебе', COLOR_LIME, FONT_LARGE, 0.4),
            ('перевести твоё число', COLOR_WHITE, FONT_LARGE, 0.5),
            ('из одной системы счисления', COLOR_LIME, FONT_LARGE, 0.6),
            ('в любую другую', COLOR_WHITE, FONT_LARGE, 0.7)
        ],
        'buttons': [
            ('Выйти', 'exit', 0.35),
            ('Вперёд!', 'rules', 0.65)
        ]
    },
    'RulesPage': {
        'labels': [
            ('Систем счисления существует множество', COLOR_WHITE, FONT_SMALL, 0.05),
            ('но здесь используются 4 основные:', COLOR_WHITE, FONT_SMALL, 0.1),
            ('Двоичная: (0, 1)', COLOR_LIME, FONT_MEDIUM, 0.2),
            ('Восьмеричная: (0-7)', COLOR_LIME, FONT_MEDIUM, 0.3),
            ('Десятичная: (0-9)', COLOR_LIME, FONT_MEDIUM, 0.4),
            ('Шестнадцатеричная: (0-9)\n(A, B, C, D, E, F)', COLOR_LIME, FONT_MEDIUM, 0.52),
            ('Число, которое ты вводишь, и которое получаешь', COLOR_WHITE, FONT_SMALL, 0.65),
            ('должны относиться к одной из этих систем', COLOR_WHITE, FONT_SMALL, 0.7),
            ('а при дешифровке с шагом равным 5', COLOR_WHITE, FONT_SMALL, 0.75),
            ('«Ж» превращается в «В»', COLOR_WHITE, FONT_SMALL, 0.8)
        ],
        'buttons': [
            ('Выйти', 'exit', 0.35),
            ('Отлично', 'start', 0.65)
        ]
    }
}

ACTIVE_MESSAGES = {
    'waiting': [
        'Жду ответа от сервера...', 'Посылаю запрос...',
        'Нужно немного подождать...', 'Дай-ка подумать...',
        'Получаю твой ответ...'
    ],
    'loading': [
        'Генерирую цикл...',
        'Создаю всё с нуля...',
        'Очищаю всё лишнее...',
        'Отлично! Начинаем...',
        'Дай мне пару секундочек!'
    ],
    'farewell': [
        'До новых встреч!',
        'Заглядывай ко мне ещё!',
        'Был рад поработать с тобой!',
        'Ты это, заходи, если что...',
        'Надеюсь, еще увидимся!'
    ]
}