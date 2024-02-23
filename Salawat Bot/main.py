import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime
TOKEN = '6921240132:AAGlh9ssc8Uj36u28yLK1nf5uMqyIDNXgvg'

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
            if datetime.now().strftime("%H:%M") == '7:30':
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                # с благовленной пятницей салават
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '09:30':
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '11:30':
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '13:30':
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '15:30':
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '17:30':
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55)
            elif datetime.now().strftime("%H:%M") == '19:30':
                await send_notification(
                    text='<strong>Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад</strong>')
                await asyncio.sleep(60 * 55 * 12)
            await asyncio.sleep(15)

# Добавить новую асинхронную функцию проверки пятницы


async def main() -> None:
    loop = asyncio.get_event_loop()
    loop.create_task(salavat_sender())
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    print('Бот запустился')
    asyncio.run(main())
    print('Бот выключен')
