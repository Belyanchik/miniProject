import telebot
import discord
from discord.ext import commands
import threading
from requests import get

PREFIX = "-"

ds = commands.Bot(command_prefix = PREFIX, intents = discord.Intents.all())
ds.remove_command("help")

DSCHANNEL = ""  #id of the Discord channel from which messages will be sent to Telegram group (Remove the quotes, place for int type)
TGGROUP = ""    #id of the Telegram group from which messages will be sent to the Discord channel (Remove the quotes, place for int type)
IDBOTDS = ""    #id of your Discord bot, it is necessary that the message is not sent twice (Remove the quotes, place for int type)

TGTOKEN = ""    #Your Telegram Bot Token
DSTOKEN = ""    #Your Discord Bot Token

tg = telebot.TeleBot(TGTOKEN)

@ds.event
async def on_message(message):
    idchannel = message.channel.id
    if(idchannel == DSCHANNEL):
        id_user = message.author.id
        if(id_user != IDBOTDS):
            name = message.author.name
            tag = message.author.discriminator
            msg = message.content
            atta = message.attachments
            if(len(atta) == 0):
                tg.send_message(TGGROUP, f"""*{name}#{tag}*

{msg}""", parse_mode= "Markdown")
            else:
                tg.send_message(TGGROUP, f"""*{name}#{tag}*

{msg}""", parse_mode= "Markdown")
                for i in range(len(atta)):
                    check = str(atta[i])
                    checknew = check[-3:]
                    if(checknew == "jpg" or checknew == "png" or checknew == "peg"):    #Media files are sent only from Discord to Telegram
                        tg.send_photo(TGGROUP, get(atta[i]).content)
                    elif(checknew == "mp4"):
                        tg.send_video(TGGROUP, get(atta[i]).content)
                    elif(checknew == "mp3"):
                        tg.send_audio(TGGROUP, get(atta[i]).content)
                    else:
                        tg.send_message(TGGROUP, atta[i])



@tg.message_handler(commands = ["id"])
def id(message):
    tg.send_message(message.chat.id, message.chat.id)

@tg.message_handler(content_types = ["text"])
def get_text(message):
    hierid = message.chat.id
    if(hierid == TGGROUP):
        text = message.text
        if(text != None):
            name = message.from_user.first_name
            nick = message.from_user.username
            if (nick == None):
                nick = "None"
            dssend(text, name, nick)

def dssend(text, name, nick):
    emb = discord.Embed(title=f"{text}", color=0x0088cc)
    emb.set_footer(text = f"{name} | @{nick}")
    channel = ds.get_channel(DSCHANNEL)
    ds.loop.create_task(channel.send(embed = emb))



def dsstart():
    ds.run(DSTOKEN)

def tgstart():
    tg.polling(none_stop = True, interval = 0)

th1 = threading.Thread(target = dsstart)

th2 = threading.Thread(target = tgstart)

if __name__ == '__main__':
    th1.start(), th2.start()
    th1.join(), th2.join()
