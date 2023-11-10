import logging
import asyncio

from aioviber import Bot, BotConfiguration, Dispatcher
from aioviber.types import Message, Keyboard, KeyboardButton
from aioviber.filters import TextFilter, StateFilter
from aioviber.fsm.context import FSMcontext

from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest

logging.basicConfig(level=logging.INFO)

bot = Bot(BotConfiguration(
    auth_token='51ed73af39e7df6f-464c10cfb2db1331-bb07310377c2c40b',
    name='DE corp1 test bot',
    avatar=''
))

dp = Dispatcher(bot=bot)


@dp.messages(TextFilter('test'))
async def echo(message: Message, state: FSMcontext):
    await state.set_state('new_state')
    message.answer(
        "Хай, круто !\nTest",
        keyboard=Keyboard(
            buttons=[KeyboardButton(
                text='тест',
                action_type='reply',
                bg_color='#000000',
                column=3
            ),KeyboardButton(
                text='тест1',
                action_type='reply',
                column=3
            )]
        ).to_json()
    )

@dp.messages(StateFilter('new_state'))
async def echo(message: Message, state: FSMcontext):
    message.copy_to(message.user.id)

    await state.clear()



@dp.conversation_started()
async def start(started: ViberConversationStartedRequest):
    bot.send_messages(
        started.user.id,
        TextMessage(
            text=f'Ласкаво просимо, {started.user.name}!\n'
        )
    )


async def main():
    await dp.start_webhook(
        path='/viber/decorptest/update'
    )

asyncio.run(main())