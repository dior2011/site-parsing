import asyncio
import logging
import sys 
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery,FSInputFile
from parsersite import parsing

TOKEN = "6232855682:AAG-6BbtpsJND2WkXXGjG-UjgHNNvgU4WfY"
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum! Saytning URLini tashlang!")


@dp.message(F.text)
async def send_text(message: Message):
    prs = parsing(message.text)
    txt = FSInputFile("C:/Users/Surf_X/Documents/I_Sifat_darslar/my_programs/parser_site/parsed.txt")
    await message.answer_document(document=txt)

    
    
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
