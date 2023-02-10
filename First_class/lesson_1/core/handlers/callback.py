from aiogram import Bot
from aiogram.types import CallbackQuery


# async def select_school(call: CallbackQuery, bot: Bot):
#     print('Callback')
#     language = call.data.split('_')[0]
#     school = call.data.split('_')[1]
#     answer_ = f'Tи обрав навчання на курсах {school} ' \
#               f'за напрямом {language.title()}-розробка'
#     await call.message.answer(answer_)
#     await call.answer()

async def select_answer(call: CallbackQuery, bot: Bot):

    answer_ = call.data
    await call.message.answer(answer_)
    await call.answer()
