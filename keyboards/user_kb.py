from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

async def user_kb():
    user_kb_list = [
        [KeyboardButton(text='Задать вопрос'), KeyboardButton(text='Рассказать историю')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=user_kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard