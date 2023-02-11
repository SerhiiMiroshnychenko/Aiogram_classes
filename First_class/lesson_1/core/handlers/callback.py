from aiogram import Bot
from aiogram.types import CallbackQuery
from ..utils.callbackdata import MacInfo


# async def select_macbook(call: CallbackQuery, bot: Bot):
#     model = call.data.split('_')[1]
#     size = call.data.split('_')[2]
#     chip = call.data.split('_')[3]
#     year = call.data.split('_')[4]
#     answer_ = f'Tи обрав Aplle Macbook {model} з діагоналлю {size} дюймів, ' \
#               f'на чіпі {chip} {year} року.'
#     await call.message.answer(answer_)
#     await call.answer()


async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MacInfo):
    model = callback_data.model
    size = callback_data.size
    chip = callback_data.chip
    year = callback_data.year
    answer_ = f'Tи обрав Aplle Macbook {model} з діагоналлю {size} дюймів, ' \
              f'на чіпі {chip} {year} року.'
    await call.message.answer(answer_)
    await call.answer()


async def select_answer(call: CallbackQuery, bot: Bot):

    answer_ = call.data
    await call.message.answer(answer_)
    await call.answer()
