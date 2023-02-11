from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Macbook Air 13" M1 2020',
            callback_data='apple_air_13_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 14" M1 Pro 2021',
            callback_data='apple_pro_14_m1_2021'
        )
    ],
    [
        InlineKeyboardButton(
            text='Apple MacBook Pro 16" 2019',
            callback_data='apple_pro_16_i7_2019'
        )
    ]
])

select_answers = InlineKeyboardMarkup(inline_keyboard=[
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


def get_macbook_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook Air 13" M1 2020', callback_data='apple_air_13_m1_2020')
    keyboard_builder.button(text='Macbook Pro 14" M1 Pro 2021', callback_data='apple_pro_14_m1_2021')
    keyboard_builder.button(text='Apple MacBook Pro 16" 2019', callback_data='apple_pro_16_i7_2019')

    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()
