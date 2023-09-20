import language_setup

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def update():
    # Main Menu:
    global main_menu

    main_menu = InlineKeyboardMarkup(resize_keyboard=True)
    main_menu.row(InlineKeyboardButton(text=language_setup.continue_text,
                                       callback_data='continue'))
    main_menu.row(InlineKeyboardButton(text=language_setup.change_language_button_text,
                                       callback_data='change-lang'))

    # Language Menu:
    global lang_menu

    lang_menu = InlineKeyboardMarkup(resize_keyboard=True)
    lang_menu.row(InlineKeyboardButton(text=language_setup.finnish_lang_button_text,
                                       callback_data='finnish-lang'))
    lang_menu.row(InlineKeyboardButton(text=language_setup.chinese_lang_button_text,
                                       callback_data='chinese-lang'))
    lang_menu.row(InlineKeyboardButton(text=language_setup.english_lang_button_text,
                                       callback_data='english-lang'))
