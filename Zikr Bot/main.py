import asyncio
from data import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime

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


async def sender() -> None:
    while True:
        if datetime.now().strftime("%H:%M") == '07:10':
            await send_notification(text='<strong>Ля Иляhа ИлляЛлаh Мухьаммадур РосулюЛлаh</strong>\nНет божества, достойного (поклонения) кроме Аллаха, Мухаммад — Посланник Аллаха')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '08:10':
            await send_notification(text='<strong>Aллаху Акбар</strong>\nАллах велик')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '09:10':
            await send_notification(text='<strong>Ля Хьавля Ва Ля Къуввата Илля БиЛляh</strong>\nНет силы и мощи кроме как у Аллаха')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '10:10':
            await send_notification(text='<strong>СубхьанаЛлаh</strong>\nПречист Аллах')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '11:10':
            await send_notification(text='<strong>АстагIфируЛлаhи Ва атубу илайхьи</strong>\nПрошу прощение у Аллаха и приношу свое покаяние и признаю, что Он мой Господь')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '12:10':
            await send_notification(text='<strong>АльхьамдулиЛляh</strong>\nХвала Аллаху')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '13:10':
            await send_notification(text='<strong>СубхьанаЛлаhи Ва Бихьамдиhи</strong>\nПречист Аллах, Велик Он, хвала Ему')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '14:10':
            await send_notification(text='<strong>СубхьанаЛлаhиль IазIым</strong>\nCлава Аллаху Великому!')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '15:10':
            await send_notification(text='<strong>Aллаху Акбар</strong>\nАллах велик')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '16:10':
            await send_notification(text='<strong>СубхьанаЛлаh</strong>\nПречист Аллах')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '17:10':
            await send_notification(text='<strong>АльхьамдулиЛляh</strong>\nХвала Аллаху')
            await asyncio.sleep(60 * 55)
        elif datetime.now().strftime("%H:%M") == '18:10':
            await send_notification(text='<strong>АстагIфируЛлаh</strong>\nО Аллах! Прости меня')
            await asyncio.sleep(60 * 55)
        #     19:10 на наше время 22:10
        elif datetime.now().strftime("%H:%M") == '19:10':
            await send_notification(text='<strong>Ля иляhа илляЛлаhу вахьдаhу ля шарика ляhу, ляhуль мульку ва ляхьуль хьамду ва hува 1аля кулли шайин къодиир</strong>\nНет божества, кроме единого Аллаха, у Которого нет сотоварищей. Ему принадлежит власть и хвала. Он способен на всякую вещь')
            await asyncio.sleep(60 * 55 * 12)
        await asyncio.sleep(15)


            
async def main() -> None:
    loop = asyncio.get_event_loop()
    loop.create_task(sender())
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    print('Бот запустился')
    asyncio.run(main())
    print('Бот выключен')
