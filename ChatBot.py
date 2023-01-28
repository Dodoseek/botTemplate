import logging
import asyncio
from aiogram import Bot, Dispatcher
from django.conf import settings

from robot.handlers import mainCommands

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



# Запуск бота
async def main():


    dp = Dispatcher()

    bot = Bot(token=settings.BOT_TOKEN)

    dp.include_router(mainCommands.router)

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
