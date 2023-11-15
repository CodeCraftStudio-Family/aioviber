import asyncio

from aiober import Bot, Dispatcher
from aiober.types import Message

bot = Bot('AUTH-TOKEN')
dp = Dispatcher(bot=bot)

# router
@dp.messages()
async def echo(message: Message):
    await message.copy_to(message.sender.id)


async def main():

    # start webhook
    await dp.start_webhook(
        host='127.0.0.1',
        port=8000,
        path='/viber/decorptest/update'
    )

asyncio.run(main())