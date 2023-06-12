import telebot
from telebot import types
import os
import time
TOKEN = '6019152480:AAFXsZ7pSp6FiOVX7aHTQb_-M0yYoEgjNXE'
bot = telebot.TeleBot(TOKEN)
decision = True
base = 'C:\\Users\\Brux\\Desktop\\test_folder\\The_base_bot'
os.chdir('C:\\Users\\Brux\\Desktop\\test_folder\\The_base_bot')


@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id,"The manual:\nIf you want to return to start you can to write '/exit' this command will remove all history and return you to chice\nsign in or sign up ")


@bot.message_handler(commands = ['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('sign in',callback_data = 'sign in'))
    markup.add(types.InlineKeyboardButton('sign up', callback_data='sign up'))

    bot.send_message(message.chat.id,'Hello welcome to Korazon base.',reply_markup=markup)


@bot.message_handler(commands = ['exit'])
def exit(message):
    global decision
    number = message.message_id
    try:
        while True:
            bot.delete_message(message.chat.id,number)
            number-=1
    except:
        pass

    if decision == False:
        os.chdir('..')
    decision = True
    return


@bot.callback_query_handler(func = lambda callback:True)
def enter(callback):
    if callback.data in ['sign in','sign up']:
        if not decision:
            bot.send_message(callback.message.chat.id,'you are already in your profile')
            return
        if callback.data == 'sign in':
            bot.send_message(callback.message.chat.id,'Well, if you want to sign in you have to give me\nyour name, and password.')
            bot.register_next_step_handler(callback.message,try_sign_in)

        elif callback.data == 'sign up':
            bot.send_message(callback.message.chat.id,'Well, if you want to sign up you have to give me\nyour name, and password.')
            bot.register_next_step_handler(callback.message,try_sign_up)

    elif callback.data in ['push','get','remove']:
        if callback.data == 'push':
            bot.send_message(callback.message.chat.id,'to push a photo in Korazon base you have to send me a name\nof the picture.')
            bot.register_next_step_handler(callback.message,push)

        elif callback.data == 'get':
            bot.send_message(callback.message.chat.id,'to get a photo in Korazon base you have to send me a name\nof the picture.')
            bot.register_next_step_handler(callback.message, get)

        elif callback.data == 'remove':
            bot.send_message(callback.message.chat.id,'to remove a photo in Korazon base you have to send me a name\nof the picture.')
            bot.register_next_step_handler(callback.message, remove)

def try_sign_up(message):
    global decision

    name_up = message.text.split()
    if name_up[0] == '/exit':

        return exit(message)

    if len(name_up) == 1:
        bot.send_message(message.chat.id,'you have to send me name and password space separated')
        bot.register_next_step_handler(message, try_sign_up)
        return
    for i in os.listdir():

        if name_up[0] == i.split('_')[0] or name_up[1] == i.split('_')[1]:
            bot.send_message(message.chat.id,'Sorry, but I already have the user with this name or password\ntry again.')
            bot.register_next_step_handler(message,try_sign_up)
            return

    bot.send_message(message.chat.id,'Now, I registered you on Korazon base\ngo in your new profile.')
    new_user = f'{name_up[0]}_{name_up[1]}'
    os.mkdir(new_user)
    os.chdir(new_user)
    decision = False
    time.sleep(3)
    functional(message)


def try_sign_in(message):
    global decision

    name_in = message.text.split()
    if name_in[0] == '/exit':
        return exit(message)

    if len(name_in) == 1:
        bot.send_message(message.chat.id,'you have to send me name and password space separated')
        bot.register_next_step_handler(message, try_sign_in)
        return
    for i in os.listdir():
        if i == name_in[0]+'_'+name_in[1]:
            bot.send_message(message.chat.id,'Ok, i found your profile\ngo in your profile.')
            os.chdir(i)
            decision = False
            time.sleep(3)
            functional(message)

            return
    bot.send_message(message.chat.id, 'No, i did not find your profile\ntry again.')
    bot.register_next_step_handler(message, try_sign_in)
    return


def push(message):
    if message.text == 'stop push':
        functional(message)
        return
    def photo_for_push(message):
        try:
            if message.text == 'stop push':
                functional(message)
                return
        except:pass
        file_info = bot.get_file(message.photo[0].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(f'{name}.jpg','wb') as file:
            file.write(downloaded_file)
            bot.send_message(message.chat.id, 'all is done')
            return

    for i in os.listdir():
        if i[0:-4] == message.text:
            bot.send_message(message.chat.id,'I already have a photo with this name.\nTry again')
            bot.register_next_step_handler(message,push)
            return
    name = message.text
    bot.send_message(message.chat.id,'Ok, send me the photo')
    bot.register_next_step_handler(message,photo_for_push)

def get(message):
    if message.text == 'stop get':
        functional(message)
        return
    for i in os.listdir():

        if i[0:-4] == message.text:
            with open(f'{message.text}.jpg','rb') as file:
                bot.send_photo(message.chat.id, file)
            return

    bot.send_message(message.chat.id, 'I do not have a photo with this name\ntry again')
    bot.register_next_step_handler(message, get)


def remove(message):
    if message.text == 'stop remove':
        functional(message)
        return
    for i in os.listdir():

        if i[0:-4] == message.text:
            os.remove(i)
            bot.send_message(message.chat.id, 'all is done')
            return

    bot.send_message(message.chat.id, 'I do not have a photo with this name\ntry again')
    bot.register_next_step_handler(message, remove)



def functional(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('push photo', callback_data='push'))
    markup.add(types.InlineKeyboardButton('get photo', callback_data='get'))
    markup.add(types.InlineKeyboardButton('remove photo', callback_data='remove'))
    bot.send_message(message.chat.id, 'What du you want to do?', reply_markup=markup)


bot.polling(none_stop = True)




