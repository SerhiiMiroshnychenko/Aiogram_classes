from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


select_school = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Україна',
            callback_data='понад усе!'
        )
    ],
    [
        InlineKeyboardButton(
            text='Маріуполь',
            callback_data='це Україна!'
        )
    ],
    [
        InlineKeyboardButton(
            text='Віримо',
            callback_data='в ЗСУ!'
        )
    ],
    [
        InlineKeyboardButton(
            text='Хороші руські',
            url='https://russianwarship.rip/'
        )
    ],
    [
        InlineKeyboardButton(
            text='Супротив',
            url='https://t.me/mrplsprotyv'
        )
    ]
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Україна', callback_data=' ...понад усе!')
    keyboard_builder.button(text='Маріуполь', callback_data=' ...це Україна!')
    keyboard_builder.button(text='Віримо', callback_data=' ...в ЗСУ!')
    keyboard_builder.button(text='Хороші руські', url='https://russianwarship.rip/')
    keyboard_builder.button(text='Супротив', url='https://t.me/mrplsprotyv')

    keyboard_builder.adjust(1, 1, 1, 2)
    return keyboard_builder.as_markup()
