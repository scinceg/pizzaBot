from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

rezhim_btn = KeyboardButton('/Режим работы')
mesto_btn = KeyboardButton('/Расположение')
menu_btn = KeyboardButton('/Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(menu_btn).row(rezhim_btn, mesto_btn)

