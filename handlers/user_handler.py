from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.user_kb import user_kb

user_router = Router()

class Form(StatesGroup):
    history = State()
    name = State()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать! Выберите, что вы хотите рассказать, историю или задать вопрос?',
                         reply_markup= await user_kb())

@user_router.message(F.text == "Рассказать историю")
async def send_history(message: Message, state: FSMContext):
    await state.set_state(Form.history)
    await message.answer('Напиши свою историю!')

@user_router.message(Form.history)
async def get_history(message: Message, state: FSMContext):
    await state.update_data(history=message.text)
    await state.set_state(Form.name)
    await message.answer('Спасибо за историю! Как тебя зовут?')


@user_router.message(Form.name)
async def get_name(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    await message.answer(f"Спасибо, {data['name']}! Ваша история принята.")



@user_router.message(F.text == 'Задать вопрос')
async def send_question(message: Message):
    await message.answer('Задай вопрос, который получат администраторы для рассмотрение')