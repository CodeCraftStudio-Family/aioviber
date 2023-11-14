import logging
import asyncio

from aiober import Bot, Dispatcher
from aiober.types import Message, Keyboard, KeyboardButton, ConversationStarted
from aiober.filters import TextFilter, StateFilter
from aiober.fsm.context import FSMcontext


logging.basicConfig(level=logging.INFO)

bot = Bot(
    '51ed73af39e7df6f-464c10cfb2db1331-bb07310377c2c40b'
)

dp = Dispatcher(bot=bot)


@dp.messages(TextFilter('test'))
async def echo(message: Message, state: FSMcontext):
    await message.answer('new test))', Keyboard(Buttons=[KeyboardButton(Text='тест')]))
    
@dp.messages()
async def echo(message: Message, state: FSMcontext):
    await message.copy_to(message.sender.id)


async def main():
    await dp.start_webhook(
        path='/viber/decorptest/update'
    )

asyncio.run(main())