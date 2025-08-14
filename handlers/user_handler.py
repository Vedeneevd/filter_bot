from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message


from keyboards.user_kb import user_kb

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать! Выберите, что вы хотите рассказать, историю или задать вопрос?',
                         reply_markup= await user_kb())

@user_router.message(F.text == "Рассказать историю")
async def send_history(message: Message):
    await message.answer('Напиши свою историю!')


@user_router.message(F.text == 'Задать вопрос')
async def send_question(message: Message):
    await message.answer('Задай вопрос, который получат администраторы для рассмотрение')