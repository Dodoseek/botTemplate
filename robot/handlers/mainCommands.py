from aiogram import Router
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer(f'👋 <i>Привет,</i> <b>{message.from_user.full_name}</b>! <i>Это Анонимный чат Телеграмма.</i>\n'
                         f'<i>Он создан для переписки 1 на 1 со случайными людьми.\n\n'
                         f'📖 В чате есть правила поведения, которые нужно соблюдать:</i>\n'
                         f'<strong>Нельзя спамить, продвигать свои услуги, оскорблять собеседников.</strong>\n\n'
                         f'🔎 <i>Для того, чтобы начать поиск собеседника, введите команду</i> /search '
                         f'<i>Будьте вежливы к собеседникам и приятного общения!</i>', parse_mode='HTML'
                         )
