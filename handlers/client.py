from aiogram import types, Dispatcher
from telegram import replymarkup
from keyboards import kb_client
from create_bot import dp, bot
from data_base import sqlite_db


async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_from_GendaBot')

async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['режим'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])