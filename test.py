import asyncio

from aioviber import Bot, BotConfiguration, Dispatcher
from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberMessageRequest, ViberConversationStartedRequest

bot = Bot(BotConfiguration(
    auth_token='...',
    name='DE corp1 test bot',
    avatar=''
))

dp = Dispatcher(bot=bot)

@dp.messages()
async def echo(message: ViberMessageRequest):
    bot.send_messages(message.sender.id, [message.message])

@dp.conversation_started()
async def start(started: ViberConversationStartedRequest):
    bot.send_messages(
        started.user.id,
        TextMessage(text=f'Ласкаво просимо, {started.user.name}!\n')
    )


async def main():

    await dp.start_webhook(
        path='/viber/decorptest/update',
        domain='...'
    )

asyncio.run(main())