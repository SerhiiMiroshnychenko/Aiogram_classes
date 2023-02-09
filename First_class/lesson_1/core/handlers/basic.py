from aiogram import Bot
from aiogram.types import Message
import json

async def get_start(message: Message, bot: Bot):
    """Обробка натискання користувача на кнопку старт"""

    # Повідомлення користувачу по id
    await bot.send_message(message.from_user.id, f'<b>Привіт {message.from_user.id}. Приємно тебе бачити!</b>')
    # Повідомлення користувачу без id => в той же чат, звідки отримали повідомлення
    await message.answer(f'<s>Привіт {message.from_user.id}. Приємно тебе бачити!</s>')
    # За допомогою reply можна цитувати повідомлення користувача
    await message.reply(f'<tg-spoiler>Привіт {message.from_user.id}. Приємно тебе бачити!</tg-spoiler>')


async def get_photo(message: Message, bot: Bot):
    """
    Реакція на надсилання користувачем картинки
    та її збереження
    """

    await message.answer(f'Відмінно, ти відправив картинку. Я збережу її собі')
    file_ = await bot.get_file(message.photo[-1].file_id)  # Зберігаємо об'єкт "file"
    # в атрибуті "photo" ми маємо три варіанти картинки різного розміру
    # отримаємо останній => найбільшого розміру

    await bot.download_file(file_.file_path, 'photo.jpg')  # Завантажуємо файл з указанням його ім'я
    # та (за необхідності) шляху куди файл зберігати


async def write_file(content):
    with open('message_arg.json', 'w') as f:
        json.dump(content, f, indent=4, default=str)
        # print(content)


async def get_hello(message: Message, bot: Bot):
    """
    Реакція на повідомлення з текстом "Привіт"
    """
    await message.answer(f'І тобі привіт!')
    # json_str = json.dumps(message.dict(), default=str)
    json_message = message.dict()
    await write_file(json_message)


