import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
import database as db

async def main():
    bot = Bot(token='6864204521:AAEayzuhGNmPTO6Vrj6YUyeaZhvxRvRDFJE')
    dp = Dispatcher()
    dp.include_router(router)
    await  db.start()
    await dp.start_polling(bot)

asyncio.run(main())