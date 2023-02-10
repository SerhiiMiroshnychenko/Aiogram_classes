from aiogram.types import Message
from aiogram import Bot


async def get_contact(message: Message, bot: Bot):
    if message.contact.user_id == message.from_user.id:
        await message.answer(f'Ти відправив <b>свій</b> контакт:  <b>+{message.contact.phone_number}</b>.')
    else:
        await message.answer(f'Ти відправив <b>не свій</b> контакт:  <b>+{message.contact.phone_number}</b>.')
