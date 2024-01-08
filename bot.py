#Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ
import os, asyncio
import requests, wget
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from PIL import Image, ImageEnhance, ImageOps
from pyrogram import Client, filters
from sh_bots.font_list import Font
from pyrogram.types import *
from telegraph import upload_file

# Retrieve your Telegram API credentials and bot token
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

API = "https://apis.xditya.me/lyrics?song="

# Initialize the Pyrogram client
app = Client(
    "image_editor_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Function to handle /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name}❤️ Welcome! Send me an image and choose an action",reply_to_message_id = message.id ,  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢" ,url=f"https://t.me/Sunrises24BotUpdates") ],
                    [
                    InlineKeyboardButton("𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 🧑🏻‍💻" ,url="https://t.me/Sunrises_24") ],
                    [
                    InlineKeyboardButton("𝐂𝐇𝐀𝐍𝐍𝐄𝐋 🎞️" ,url="https://t.me/sunriseseditsoffical6") ]                               
            ]))
   
print("Bot Started!🦋 © t.me/Sunrises_24")

# Function to handle /help command
@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = """
    <b>Hᴇʟʟᴏ Mᴀᴡᴀ ❤️
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.

🦋 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Photo 🖼️

/grayscale - 𝐶𝑜𝑛𝑣𝑒𝑟𝑡 𝑖𝑚𝑎𝑔𝑒 𝑡𝑜 𝑔𝑟𝑎𝑦𝑠𝑐𝑎𝑙𝑒
/enhance - 𝐸𝑛ℎ𝑎𝑛𝑐𝑒 𝑖𝑚𝑎𝑔𝑒
/changecolor - 𝐶ℎ𝑎𝑛𝑔𝑒 𝑃ℎ𝑜𝑡𝑜 𝐶𝑜𝑙𝑜𝑟
/resizephoto - 𝑇𝑜 𝑎𝑑𝑗𝑢𝑠𝑡 𝑡ℎ𝑒 𝑑𝑖𝑚𝑒𝑛𝑠𝑖𝑜𝑛𝑠 𝑜𝑓 𝑎𝑛 𝑖𝑚𝑎𝑔𝑒
/telegraph - 𝑇𝑜 𝑔𝑒𝑡 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑝ℎ 𝐿𝑖𝑛𝑘 🔗
/about - 𝐿𝑒𝑎𝑟𝑛 𝑚𝑜𝑟𝑒 𝑎𝑏𝑜𝑢𝑡 𝑡ℎ𝑖𝑠 𝑏𝑜𝑡

◉ ғᴏɴᴛ 
/font - 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑤𝑖𝑡ℎ 𝑡𝑒𝑥𝑡 𝑡𝑜 𝐹𝑜𝑛𝑡 🔠
Enter Any Text Eg:- /font [text]

◉ JɪᴏSᴀᴀᴠɴ
/ssong - 𝑇𝑜 𝑔𝑒𝑡 𝑡ℎ𝑒 𝑠𝑜𝑛𝑔 𝑓𝑟𝑜𝑚 𝐽𝑖𝑜𝑆𝑎𝑎𝑣𝑛🎵

◉ Lʏʀɪᴄs 
/lyrics - 𝑇𝑜 𝑔𝑒𝑡 𝑙𝑦𝑟𝑖𝑐𝑠 𝑜𝑓 𝑠𝑜𝑛𝑔𝑠 📝🎶

◉ Rᴇᴘᴏ🖇️
/repo - 𝑇𝑜 𝑠𝑒𝑎𝑟𝑐ℎ 𝑟𝑒𝑝𝑜 𝑓𝑟𝑜𝑚 𝐺𝑖𝑡𝐻𝑢𝑏 🖇️

 💭This bot is designed to apply filters to images.
 
🔱 𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 : <a href='https://t.me/Sunrises_24'>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™</a></b>
    
   """
    await message.reply_text(help_text)

# Function to handle /about command
@app.on_message(filters.command("about"))
async def about_command(client, message):
    about_text = """
<b>✯ Mʏ Nᴀᴍᴇ :  <a href=https://t.me/PHOTOENHANCER24BOT>🦋Pʜᴏᴛᴏ Eɴʜᴀɴᴄᴇʀ 𝟸𝟺 Bᴏᴛ🦋</a></b></b>
<b>✯ Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻 : <a href=https://t.me/Sunrises_24>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™ ✨</a></b>
<b>✯ Uᴘᴅᴀᴛᴇs 📢 : <a href=https://t.me/Sunrises24BotUpdates>𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢</a></b>
<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs 📊 : ᴠ2 [Sᴛᴀʙʟᴇ]</b>
    """
    await message.reply_text(about_text)
    
# Function to handle /grayscale command
@app.on_message(filters.command("grayscale"))
async def grayscale_command(client, message):
    if message.reply_to_message:
        photo = await message.reply_to_message.download()
        grayscale_image = convert_to_grayscale(photo)
        grayscale_image_path = "grayscale_" + str(message.chat.id) + ".png"
        grayscale_image.save(grayscale_image_path)
        await message.reply_photo(
            photo=grayscale_image_path,
            caption="Grayscale filter applied!"
        )
        os.remove(grayscale_image_path)
    else:
        await message.reply_text("Please reply to an image to apply the grayscale filter.")

# Function to convert image to grayscale
def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    return grayscale_image

# Function to handle /enhance command
@app.on_message(filters.command("enhance"))
async def enhance_command(client, message):
    if message.reply_to_message:
        photo = await message.reply_to_message.download()
        enhanced_image = enhance_image(photo)
        enhanced_image_path = "enhanced_" + str(message.chat.id) + ".png"
        enhanced_image.save(enhanced_image_path)
        await message.reply_photo(
            photo=enhanced_image_path,
            caption="Enhanced image!"
        )
        os.remove(enhanced_image_path)
    else:
        await message.reply_text("Please reply to an image to apply enhancement.")
        
# Function to enhance an image
def enhance_image(image_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(1.5)  # Adjust enhancement factor as needed
    return enhanced_image

# Function to handle /changeshirtcolor command
@app.on_message(filters.command("changecolor"))
async def changecolor_command(client, message):
   if message.reply_to_message:
       photo = await message.reply_to_message.download()
       new_color = change_color(photo)
       new_color_path = "new_color_" + str(message.chat.id) + ".png"
       new_color.save(new_color_path)
       await message.reply_photo(
           photo=new_color_path,
           caption="Photo color changed!"
       )
       os.remove(new_color_path)
   else:
       await message.reply_text("Please reply to an image to apply Photo Colour.")
        
# Function to change Photo color
def change_color(image_path, new_color=(255, 0, 0)):
    image = Image.open(image_path)
    # Assuming the shirt is red, changing the color to a new_color
    image = ImageOps.colorize(image.convert('L'), black="black", white=new_color)
    return image
    
# Function to Font 
@app.on_message(filters.command("font"))
async def stylize_text(client, message):      
       text_to_stylize = message.text.split(" ", 1)[1]  
       stylized_text = Font.SH(text_to_stylize)  

       await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴛᴇxᴛ: <code>{stylized_text}</code>")
   
# Function to Telegraph 
@app.on_message(filters.command("telegraph"))
async def telegraph_upload(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("Ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ or ᴠɪᴅᴇᴏ.")
    if not ( replied.photo or replied.video ):
        return await message.reply_text("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀ ᴠᴀʟɪᴅ ᴍᴇᴅɪᴀ")
    text = await message.reply_text("<code>Downloading...</code>", disable_web_page_preview=True)   
    media = await replied.download()   
    await text.edit_text("<code>ᴜᴘʟᴏᴀᴅɪɴɢ...</code>", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        return await text.edit_text(text=f"ᴇƦƦᴏƦ :- {error}\nғᴏʀᴡʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ(/support) ᴏʀ ᴀᴅᴍɪɴ(/about", disable_web_page_preview=True)          
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"https://telegra.ph{response[0]}",
        disable_web_page_preview=True,
    )

# Function to JioSaavn
@app.on_message(filters.command('ssong') & filters.text)
async def song(client, message):
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/ssong requires an argument.")
    if args.startswith(" "):
        await message.reply("/ssong requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
  #  album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "mp3")
    os.rename(file, ffile)
    await pak.edit('Uploading...')
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers,caption=f"[{sname}]({r['data']['results'][0]['url']}) - from saavn ",thumb=thumbnail)
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()

# Function to Repo

@app.on_message(filters.command("repo"))
async def repo(client, message):
    if len(message.command) > 1:
        query = ' '.join(message.command[1:])
        response = requests.get(f"https://api.github.com/search/repositories?q={query}")
        if response.status_code == 200:
            data = response.json()
            if data['total_count'] > 0:
                repo = data['items'][0] 
                reply = f"**{repo['name']}**\n\n" \
                        f"**📝 ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:** <code>{repo['description']}</code>\n" \
                        f"**🔗 ᴜʀʟ:** {repo['html_url']}\n" \
                        f"**🌟 sᴛᴀʀs:** <code>{repo['stargazers_count']}</code>\n" \
                        f"**🪝 ғᴏʀᴋs:** <code>{repo['forks_count']}</code>"

                await message.reply_text(reply)
            else:
                await message.reply_text("ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ.")
        else:
            await message.reply_text("ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ.")
    else:
        await message.reply_text("ᴜsᴀɢᴇ: /repo {repo_name}")

# Function to handle /resizephoto command
@app.on_message(filters.command("resizephoto"))
async def resize_photo_command(client, message):
    if message.reply_to_message:
        photo = await message.reply_to_message.download()
        resized_image = resize_photo(photo)
        resized_image_path = "resized_" + str(message.chat.id) + ".png"
        resized_image.save(resized_image_path)
        await message.reply_photo(
            photo=resized_image_path,
            caption="Resized image!"
        )
        os.remove(resized_image_path)
    else:
        await message.reply_text("Please reply to an image to resize.")

# Function to resize an image
def resize_photo(image_path):
    image = Image.open(image_path)
    resized_image = ImageOps.fit(image, (300, 300))  # Adjust the size as needed
    return resized_image
   
@app.on_message(filters.command(["lyrics"])) 
async def sng(client, message):
    if not message.reply_to_message:
          await message.reply_text("Please reply to a message")
    else:          
          mee = await message.reply_text("`Searching 🔎`")
          song = message.reply_to_message.text
          chat_id = message.from_user.id
          rpl = lyrics(song)
          await mee.delete()
    try:
          await mee.delete()
          await bot.send_message(chat_id, text = rpl, reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs ", url = f"t.me/Sunrises24BotUpdates")]]))
    except Exception as e:                            
          await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"t.me/Sunrises24BotUpdates")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Sᴜᴄᴄᴇꜱꜰᴜʟʟy Exᴛʀᴀᴄᴛᴇᴅ Lyɪʀɪᴄꜱ Oꜰ {song}**\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Made By Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ**'
        return text
    
# Run the bot
app.run()
