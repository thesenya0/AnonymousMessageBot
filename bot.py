import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

# токен бота (можно получить у @BotFather)
BOT_TOKEN = 'BOT_TOKEN'

ADMIN_CHAT_ID = 123456789  # ID владельца бота / админа тгк (вписан пример)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для анономных сообщений!\n"
        "Просто отправь сообщение и я анонимно его отправлю владельцу тгк."
    )

@dp.message()
async def handle_message(message: Message):
    if message.text:
        try:
            await bot.send_message(ADMIN_CHAT_ID, message.text)
            
            await message.answer("Ваше сообщение отправлено")
        
        except Exception as e:
            await message.answer("Произошла ошибка при отправке сообщения.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
