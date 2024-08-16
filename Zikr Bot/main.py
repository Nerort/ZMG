import json
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, time, timedelta

# Uploading all data from JSON file
with open('config.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    TOKEN = data['token']
    CHANNEL_ID = data['channel_id']
    GREETING = data['greeting']
    MESSAGES = data['messages']
    SALAWAT_TEXT = data['salawat_text']

# Initializing the Bot
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


# Function for commands /help and /start
@dp.message(Command('help', 'start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(text=GREETING)


# Function for sending messages to the channel
async def send_notification(text: str) -> None:
    await bot.send_message(text=text, chat_id=CHANNEL_ID)


# Schedule for posts in the main channel
def schedule_messages(scheduler: AsyncIOScheduler) -> None:
    for item in MESSAGES:
        time_str = item['time']
        message = item['message']
        hour, minute = map(int, time_str.split(':'))
        scheduler.add_job(
            send_notification,
            "cron",
            hour=hour,
            minute=minute,
            args=[message]
        )


# Sending salawats on Friday
async def salavat_sender():
    salavat_times = [time(7, 30), time(9, 30), time(11, 30), time(13, 30), time(15, 30)]
    while True:
        now = datetime.now()
        if now.weekday() == 4:  # now.weekday() == 4 means Friday
            for salavat_time in salavat_times:
                if salavat_time <= now.time() < (datetime.combine(now, salavat_time) + timedelta(minutes=1)).time():
                    await send_notification(text=SALAWAT_TEXT)
                    await asyncio.sleep(60)  # sleep for 1 minute to avoid duplicate messages

        await asyncio.sleep(15)  # check every 15 seconds


async def main() -> None:
    scheduler = AsyncIOScheduler()
    schedule_messages(scheduler)
    scheduler.start()
    asyncio.create_task(salavat_sender())
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    print('Бот запущен')
    asyncio.run(main())
    print('Бот отключен')
