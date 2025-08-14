import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
import dotenv
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

dotenv.load_dotenv()

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    try:
        logger.info("Бот запускается...")
        await dp.start_polling(bot)
        logger.info("Бот начал работу")
    except Exception as e:
        logger.error(f"Ошибка в работе бота: {e}", exc_info=True)
    finally:
        logger.info("Завершение работы бота...")
        await bot.session.close()
        logger.info("Бот успешно остановлен")

if __name__ == '__main__':
    asyncio.run(main())