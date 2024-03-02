import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime
TOKEN = 'your token'

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(Command('help', 'start'))
async def command_start_handler(message: Message) -> None:
    """
    This handler answers on '/start' and '/help'
    """
    print('Chat info:', message.chat)
    await message.answer(text=f'Привет, меня зовут "Зикр"!\nЯ был создан, чтобы напоминать о поминании Аллаха')


async def send_notification(text: str) -> None:
    await bot.send_message(text=text, chat_id='@delay_zikr')


async def salavat_sender():
    while True:
        if datetime.isoweekday(datetime.now()) == 5:
            if datetime.now().strftime("%H:%M") == '7:30': #10:30
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '09:30': #12:30
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '11:30': #14:30
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '13:30': #16:30
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '15:30': #18:30
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55 * 9)
            await asyncio.sleep(15)


async def main() -> None:
    loop = asyncio.get_event_loop()
    loop.create_task(salavat_sender())
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    print('Бот запустился')
    asyncio.run(main())
    print('Бот выключен')
