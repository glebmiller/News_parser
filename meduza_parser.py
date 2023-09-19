from telethon import TelegramClient, events, sync
from decouple import config
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import telegram
import settings
#from telegram import ParseMode


bot_key = config("bot_key")
# Remember to use your own values from my.telegram.org!
api_id = config("API_ID")
api_hash = config('API_HASH')
meduza_ID  = config("MEDUZA_ID")
sirena_ID = config("SIRENA_ID")
MY_ID = config("MY_ID") 

KEY_WORDS = settings.KEY_WORDS
#print(api_id)
#print(api_hash)
client = TelegramClient('anon', api_id, api_hash)

bot = Bot(bot_key)
dp = Dispatcher(bot)


async def process_news(event, source, chatid):
    text = event.raw_text[:event.raw_text.find("\n")]
    text = text.strip()
    last_word = text[text.rfind(" "):]
    
    #print(text)
    #print(last_word)
    #print("event=", event)
    #print("event.message=", event.message)
    #print("event.message.id=", event.message.id)
    pics = []
    try:
        pic_id = event.message.media.photo.id
        pics.append(pic_id)
        print(pic_id)
        media = event.message.media
    except:
        print("no photo")
    markup = types.InlineKeyboardMarkup()
    URL = "https://t.me/" + source + "/" + str(event.message.id)
    text = text[:text.rfind(" ")] + f"<a href='{URL}'>{last_word}</a>"

    if pics:
        try:
            """
            media = types.MediaGroup()
            media.attach_photo(types.InputFile('media/Starbucks_Logo.jpg'), 'Превосходная фотография')
            media.attach_photo(types.InputFile('media/Starbucks_Logo_2.jpg'), 'Превосходная фотография 2')
            await bot.send_media_group(call.message.chat.id, media=media)
            """
            await bot.send_photo(chatid, pics[0])
        except:
            print('error sending pics')
    await bot.send_message(chatid, text, parse_mode="HTML", disable_web_page_preview=True)

def check_string_for_keywords(string, keyword_list):
    for keyword in keyword_list:
        #print(keyword)
        if keyword in string:
            return True
    return False



async def process_telegram_posts(event, source, chatid):
    #text = event.raw_text[:event.raw_text.find("\n")]
    #text = event.message

    text = event.message.message

    #print(type(event))
    print(event)
    #print(text)
    #print(check_string_for_keywords(text, KEY_WORDS))

    if check_string_for_keywords(text, KEY_WORDS):
        print("The string contains one of the keywords.")
        user_id = event.original_update.message.from_id.user_id
        print(user_id)
        await client.send_message(user_id, "у меня есть то, что вам нужно")

    else:
        print("The string does not contain any of the keywords.")



@client.on(events.NewMessage(chats="news_sirena"))
async def sirena_handler(event):
    await process_news(event, "news_sirena", sirena_ID)

@client.on(events.NewMessage(chats='meduzalive'))
async def meduza_handler(event):
    await process_news(event, "meduzalive", meduza_ID)
    
@client.on(events.NewMessage(chats='my_bot_testing_group'))
async def meduza_handler(event):
    await process_telegram_posts(event, "my_bot_testing_group", MY_ID)


client.start()
client.run_until_disconnected()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
