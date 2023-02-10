from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# ReplyKeyboardMarkup - для створення клавіатури
# KeyboardButton - для створення кнопки
# KeyboardButtonPollType - для створення опитувань чи вікторин

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ряд 1. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 1. Кнопка 2'
        )
    ],
    [
        KeyboardButton(
            text='Ряд 2. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 2. Кнопка 2'
        )
    ],
    [
        KeyboardButton(
            text='Ряд 4. Кнопка 1'
        )
    ],
])

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Відправити геолокацію',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='Відправити свій контакт',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Створити вікторину',
            request_poll=KeyboardButtonPollType()  # type='quiz' -> створення вікторини,
            # type='regular' -> створення опитування з декількома результатами відповідей
        )
    ],
])


def get_reply_keyboard():
    """
    Функція для формування текстової клавіатури
    """
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Привіт!')
    keyboard_builder.button(text='Слава Україні!')
    keyboard_builder.button(text='Відправити геолокацію', request_location=True)
    keyboard_builder.button(text='Відправити свій контакт', request_contact=True)
    keyboard_builder.button(text='Створити опитування', request_poll=KeyboardButtonPollType())

    # За допомогою методу adjust визначимо скільки кнопок буде в кожному ряду (перший 2, другий 2, третій 1)
    keyboard_builder.adjust(2, 2, 1)

    return keyboard_builder.as_markup()



