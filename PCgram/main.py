import telebot
import pyscreenshot
import os
import webbrowser

import config
file = open("alltext.txt", "r", encoding = "utf-8")
text = file.read().split(";")

client = telebot.TeleBot(config.config["TOKEN"])

@client.message_handler(commands = ["start"])
def start_commands(message):
    client.send_message(message.chat.id, config.config["ERROR_MSG"])

@client.message_handler(commands = ["id"])
def id(message):
    client.send_message(message.chat.id, message.chat.id)

@client.message_handler(commands = ["ping"])
def ping(message):
    if(message.chat.id in config.config["WHITE_LIST"]):
        client.send_message(message.chat.id, "The computer is working")
    else:
        client.send_message(message.chat.id, config.config["ERROR_MSG"])

@client.message_handler(commands = ["screenshot"])
def screenshot(message):
    if(message.chat.id in config.config["WHITE_LIST"]):
        image = pyscreenshot.grab()
        image.save("screenshot.png")
        client.send_photo(message.chat.id, open("screenshot.png", "rb"))
        os.remove("screenshot.png")
    else:
        client.send_message(message.chat.id, config.config["ERROR_MSG"])

@client.message_handler(commands = ["all_processes"])
def all_processes(message):
    if(message.chat.id in config.config["WHITE_LIST"]):
        output = os.popen('wmic process get description').read().split()
        newlen = ""
        for i in range(len(output)):
            if (output[i][-3:] == "exe"):
                if(output[i] in config.processes):
                    if(config.processes[output[i]] not in newlen):
                        newlen = newlen + "`" + config.processes[output[i]] + "`" + "\n"
        client.send_message(message.chat.id, newlen, parse_mode = "markdown")
    else:
        client.send_message(message.chat.id, config.config["ERROR_MSG"])

@client.message_handler(commands = ["help"])
def help(message):
    if(message.chat.id in config.config["WHITE_LIST"]):
        file = open("alltext.txt", "r", encoding="utf-8")
        text = file.read().split(";")
        new = ""
        for i in text:
            new = new + i
        client.send_message(message.chat.id, new)
        file.close()
    else:
        client.send_message(message.chat.id, config.config["ERROR_MSG"])

@client.message_handler(commands = ["kill"])
def kill(message):
    if(message.chat.id in config.config["WHITE_LIST"]):
        msg = client.send_message(message.chat.id, "Enter the name of the process")
        client.register_next_step_handler(msg, giveProcess)
    else:
        client.send_message(message.chat.id, config.config["ERROR_MSG"])

def giveProcess(message):
    process = message.text
    check = False
    for i in config.processes:
        if(process == config.processes[i]):
            os.system(f"taskkill /IM {i}")
            check = True
            client.send_message(message.chat.id, "The process is terminated")
    if(check == False):
        client.send_message(message.chat.id, "A process with this name was not found")

@client.message_handler(commands = ["open"])
def openURL(message):
    if (message.chat.id in config.config["WHITE_LIST"]):
        msg = client.send_message(message.chat.id, "Send the URL")
        client.register_next_step_handler(msg, giveURL)
    else:
        client.send_message(message.chat.id, config.config["ERROR_MSG"])

def giveURL(message):
    URL = message.text
    webbrowser.open(URL)
    client.send_message(message.chat.id, "The URL is open")

client.polling(none_stop = True, interval = 0)