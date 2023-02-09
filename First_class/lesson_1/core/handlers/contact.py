from aiogram.types import Message
from aiogram import Bot

async def get_true_contact(message: Message, bot: Bot):
    await message.answer(f'Ти відправив <b>свій</b> контакт.')


async def get_fake_contact(message: Message, bot: Bot):
    await message.answer(f'Ти відправив <b>не свій</b> контакт.')
