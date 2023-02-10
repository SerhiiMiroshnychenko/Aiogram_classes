from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType, Contact
import asyncio
import logging
from core.handlers.basic import get_start, get_photo, get_hello, get_glory
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_contact
from core.settings import settings
from aiogram.filters import Command, CommandStart
from core.utils.commands import set_commands
from core.handlers.basic import get_location




async def start_bot(bot: Bot):
    """Надсилає повідомлення адміну бота інформацію про старт бота"""
    await set_commands(bot)  # Викликаємо команди бота
    await bot.send_message(settings.bots.admin_id, text='Бот стартує!')

async def stop_bot(bot: Bot):
    """Надсилає повідомлення адміну бота інформацію про зупинку бота"""
    await bot.send_message(settings.bots.admin_id, text='Бот зупинено!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d - %(message)s'
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()  # Об'єкт, що займається отриманням update

    dp.startup.register(start_bot)  # Реєструємо handler "start_bot" на подію "startup" => старт бота
    dp.startup.register(stop_bot)  # Реєструємо handler "stop_bot" на подію "startup" => стоп бота

    dp.message.register(get_photo, F.photo)  # реєструємо реакцію на фото
    dp.message.register(get_location, F.location)  # реєструємо реакцію на локацію
    dp.message.register(get_hello, F.text == 'Привіт')  # реєструємо реакцію на "Привіт"
    dp.message.register(get_hello, F.text == 'Привіт!')
    dp.message.register(get_glory, F.text == 'Слава Україні')
    dp.message.register(get_glory, F.text == 'Слава Україні!')
    dp.message.register(get_contact, F.contact)

    # Реєструємо handler "get_start" на подію "message"
    dp.message.register(get_start, Command(commands=['start', 'run']))
    # dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)  # Запускаємо отримання update
    except asyncio.exceptions.CancelledError as e:
        print(e.__class__, e)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
