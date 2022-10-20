from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

def reply(sender_id, msg_text, project):
    reply_msg = f"""
    отправитель: @{sender_id}
    объект: {project}
    текст: {msg_text}
    """
    return reply_msg


TOKEN='5649056674:AAFtXRPm0vcBOEBPJGwK8SZI5X-6K1or_Hs'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

project_text = ["/Синергия", "/Грабин", "/Политех", "/АДЦ", "/Технопарк", "/Заводы"]


buttons = [KeyboardButton(button) for button in project_text]

greet_kb = ReplyKeyboardMarkup()


project = ""
check_text = False
for button in buttons:
    greet_kb.add(button)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nПо какому ОБЪЕКТУ вопрос?", reply_markup=greet_kb)

@dp.message_handler(commands=[command[1:] for command in project_text])
async def echo_message(msg: types.Message):
    global project
    global check_text
    project = msg.text
    check_text = True
    await bot.send_message(msg.from_user.id, "Пожалуйста, впишите текст обращения в одном сообщении")

@dp.message_handler(commands=["group_id"])
async def echo_message(msg: types.Message):
    await msg.reply(msg.chat.id)



@dp.message_handler()
async def echo_message1(msg: types.Message):
    global check
    if check_text:
        group_id = -0
        match project:
            case r"/Синергия":
                group_id = -875302664


        await bot.send_message(group_id, reply(msg.from_user.username, msg.text, project))
        check = False


@dp.message_handler()
async def echo_message2(msg: types.Message):
    global check
    if check_text:
        group_id = -0
        match project:
            case r"/Политех":
                group_id = -875302664



    await bot.send_message(group_id, reply(msg.from_user.username, msg.text, project))
    check = False

if __name__ == '__main__':
    executor.start_polling(dp)