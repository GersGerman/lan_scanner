import os
import sys
import asyncio
from aiogram.filters.command import Command # type: ignore
from aiogram import Bot, Dispatcher, types, F # type: ignore
from aiogram.enums.parse_mode import ParseMode # type: ignore


import requests


bot = Bot(token=sys.argv[1])

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    data = open(f"{os.getcwd()}\\telegram\\users", 'r').read().split("\n")
    if str(message.from_user.id) not in data:

        await message.answer(f"Привет, {message.from_user.username}!")
        await message.answer("Теперь, при каждом новом подключении к сети тебе будет приходить уведомление об этом, ты сможешь так же как и на сайте добавить устройство в список постоянных или удалить оттуда")
        await message.answer('Если что то не понятно пиши /help либо посмотри справку на сайте')


        data.append(str(message.from_user.id))
        if "" in data:
            data.remove("")
        
        with open("users", 'w') as file:
            Data = ""
            for i in data:
                Data = Data + i + "\n"
            print(Data)
            file.write(Data)
            file.close()
    
    else:
        await message.answer("Бот работает исправно!\nПомощь - /help")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Если тебе нужно посмотреть какие устройства на данный момент видно в сети - /scan")
    await message.answer("Получить список \n<b>Постоянных</b> устройств - /constant\n<b>новых</b> - /new_ip", parse_mode=ParseMode.HTML)

@dp.message(Command("constant"))
async def cmd_constant(message: types.Message):
    buttons = []
    for i in [['устройство 1', '192.168.1.1'], ['устройство 2', '192.168.1.2'], ['устройство 3', '192.168.1.3']]:
        buttons.append([
            types.InlineKeyboardButton(text='{} - {}'.format(i[0], i[1]), callback_data=f'delete_{i[1]}')
        ])
    
    await message.answer("Вот список постоянных устройств, нажмите на кнопку чтобы удалить его", reply_markup=types.InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.message(Command("new_ip"))
async def cmd_constant(message: types.Message):
    buttons = []
    for i in [['устройство 4', '192.168.1.4'], ['устройство 5', '192.168.1.5'], ['устройство 6', '192.168.1.6']]:
        buttons.append([
            types.InlineKeyboardButton(text='{} - {}'.format(i[0], i[1]), callback_data=f'add_{i[1]}')
        ])
    
    await message.answer("Вот список новых устройств, нажмите на кнопку чтобы запомнить и при дальнейшем их подключении сообщение не выводилось", reply_markup=types.InlineKeyboardMarkup(inline_keyboard=buttons))

@dp.callback_query()
async def callback_(callback: types.CallbackQuery):
    data = callback.data.split("_")

    if data[0] == 'delete':
        await callback.message.answer(f"Устройство {data[1]} было удалено, при повторном подключении вам придет уведомление")

    if data[0] == 'add':
        await callback.message.answer(f"Устройство {data[1]} было добавлено, при повторном подключении уведомления вам приходить не будут")

@dp.message(Command("scan"))
async def scan_network(message: types.Message):
        await message.reply("Дождитесь результата сканирования, это может занять некоторое время...")
        req = requests.get("http://127.0.0.1:8089/getdata/devices")
        data = req.json()
        
        for device in data['new']:
            await message.answer(f"{device['ip']} - {device['mac']}\n\nНовый")
        
        for device in data['old']:
            await message.answer(f"{device['ip']} - {device['mac']}\n\nРазрешенный")


async def main():
    await dp.start_polling(bot)

print("1")
asyncio.run(main())
