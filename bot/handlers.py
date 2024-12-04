from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
import database as db

router = Router()

@router.message(Command('id'))
async def id(message:Message):
    await message.answer(f'{message.from_user.id}')

@router.message(Command('kiss'), lambda message: message.reply_to_message is not None)
async def reply_handler(message:Message):
    await db.kiss(message.reply_to_message.from_user.id)
    await message.reply(f'[{message.from_user.first_name}]({message.from_user.url}) '
                        f'поцеловал(-а) [{message.reply_to_message.from_user.first_name}]({message.reply_to_message.from_user.url})', parse_mode=ParseMode.MARKDOWN)
    await message.reply_to_message.reply_sticker('CAACAgIAAxkBAAIMFGdQQ0DF55mLCD7-gKKSMlb5k1YKAAImHAAC5cyZSvgp6N9Tw5uHNgQ')

@router.message(Command('rating'))
async def rating(message: Message):
    res = ''
    users = db.cur.execute("SELECT * FROM users").fetchall()
    u = db.cur.execute('SELECT * FROM users WHERE kisses = (SELECT MAX(kisses) FROM users)').fetchone()
    if (u == None):
        await message.reply('Все любовные списки пусты!')
    else:
        user = await message.bot.get_chat(u[0])
        url = f'tg://user?id={u[0]}'
        res += f'[{user.first_name}]({url}) - самый зацелованный!\n\n'
        for u in users:
            user = await message.bot.get_chat(u[0])
            url = f'tg://user?id={u[0]}'
            res += f'[{user.first_name}]({url}) целованный(-ая) {u[1]} раз\n'
        await message.reply(res, parse_mode=ParseMode.MARKDOWN)