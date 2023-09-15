"""from telethon import TelegramClient, events, sync
from decouple import config
from aiogram import Bot, Dispatcher, executor, types
import asyncio

bot = Bot('5505110126:AAHut6yfejJSpUrp0JzNTsjn9ymStAfaonM')
dp = Dispatcher(bot)


# Remember to use your own values from my.telegram.org!
api_id = config("API_ID")
api_hash = config('API_HASH')
CHAT_ID  = config("CHAT_ID")
#print(api_id)
#print(api_hash)
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='my_test_chanel_123'))
async def my_event_handler(event):
    #print(event)
    text = event.raw_text[:event.raw_text.find("\n")]
    #print("type(event)=", type(event))
    #print("event.message=", event.message)
    #print("event.message.media.photo.id=", event.message.media.photo.id)
    pics = []
    try:
        pic_id = event.message.media.photo.id
        pics.append(pic_id)
    except:
        print("no photo")
    print(text)
    
    if pics:
        print(*pics)
        
    markup = types.InlineKeyboardMarkup()
    URL = "https://t.me/https://t.me/my_test_chanel_123/" + str(event.message.id)
    markup.add(
                        types.InlineKeyboardButton(text="Новость полностью", url=URL)
                    )
    reply_markup=markup
    #await bot.send_message(CHAT_ID, text, reply_markup=markup)

client.start()
client.run_until_disconnected()


"""

def check_string_for_keywords(string, keyword_list):
    for keyword in keyword_list:
        if keyword in string:
            return True
    return False

# Example usage
my_string = "sal,ae,eoq iquwej miqiwem"
keywords = ["sample", "test", "example"]

if check_string_for_keywords(my_string, keywords):
    print("The string contains one of the keywords.")
else:
    print("The string does not contain any of the keywords.")


