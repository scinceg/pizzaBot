from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = "5085544544:AAGdJKnGrYGAmEA95hEETeEKHJZ-zVC5-TI"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)