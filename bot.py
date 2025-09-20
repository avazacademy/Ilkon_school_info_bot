import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from handlers import start   
from config import BOT_TOKEN
from database.db import init_db
from handlers  import subjects


async def main():
    logging.basicConfig(level=logging.INFO)

    init_db()
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(start.start_router)
    dp.include_router(subjects.sub_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
