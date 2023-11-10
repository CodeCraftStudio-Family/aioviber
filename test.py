import asyncio

from aioviber import Bot, BotConfiguration, Dispatcher
from aioviber.types import Message
from aioviber.filters import TextFilter, StateFilter
from aioviber.fsm.context import FSMcontext

from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest


bot = Bot(BotConfiguration(
    auth_token='...',
    name='...',
    avatar=''
))

dp = Dispatcher(bot=bot)


@dp.messages(TextFilter('test'))
async def echo(message: Message, state: FSMcontext):
    await state.set_state('new_state')
    message.answer(
        "Хай, круто !\nTest"
    )

@dp.messages(StateFilter('new_state'))
async def echo(message: Message, state: FSMcontext):
    message.copy_to(message.user.id)

    await state.clear()



@dp.conversation_started()
async def start(started: ViberConversationStartedRequest):
    bot.send_messages(
        started.user.id,
        TextMessage(text=f'Ласкаво просимо, {started.user.name}!\n')
    )


async def main():
    await dp.start_webhook(
        path='/viber/decorptest/update'
    )

asyncio.run(main())