import logging
import asyncio

from aiober import Bot, Dispatcher
from aiober.types import Message, Keyboard, KeyboardButton, ConversationStarted
from aiober.filters import TextFilter, StateFilter
from aiober.fsm.context import FSMcontext


logging.basicConfig(level=logging.INFO)

bot = Bot(
    'AUTH-TOKEN'
)

dp = Dispatcher(bot=bot)


@dp.messages(TextFilter('test'))
async def echo(message: Message, state: FSMcontext):
    await state.set_state('test_state')
    await state.update_data(name='pedik blyt')

    await message.answer('new test))', Keyboard(Buttons=[KeyboardButton(Text='тест')]))
    
@dp.messages(StateFilter('test_state'))
async def echo(message: Message, state: FSMcontext):
    _state = await state.get_state()
    _data = await state.get_data()

    print(_state, _data)

    await state.clear()

    await message.copy_to(
        message.sender.id,
        text=f"{message.text} {_data.get('name')}"
    )


async def main():
    await dp.start_webhook(
        path='/viber/decorptest/update'
    )

asyncio.run(main())