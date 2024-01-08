#Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ
import os
from PIL import Image, ImageEnhance, ImageOps
from pyrogram import Client, filters

# Retrieve your Telegram API credentials and bot token
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

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
        "Welcome! Send me an image and choose an action",reply_to_message_id = message.id ,  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢" ,url=f"https://t.me/Sunrises24BotUpdates") ],
                    [
                    InlineKeyboardButton("𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 🧑🏻‍💻" ,url="https://t.me/Sunrises_24") ],
                    [
                    InlineKeyboardButton("𝐂𝐇𝐀𝐍𝐍𝐄𝐋 🎞️" ,url="https://t.me/sunriseseditsoffical6") ],
                    [
                    InlineKeyboardButton("𝐇𝐄𝐋𝐏 ✨" ,callback_data='help')],
                    [
                    InlineKeyboardButton("𝐀𝐁𝐎𝐔𝐓 🧑🏻‍💻" ,callback_data='about')]                    
            ]))
    
print("Bot Started!🦋 © t.me/Sunrises_24")

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
        
# Function to change shirt color
def change_color(image_path, new_color=(255, 0, 0)):
    image = Image.open(image_path)
    # Assuming the shirt is red, changing the color to a new_color
    image = ImageOps.colorize(image.convert('L'), black="black", white=new_color)
    return image
 
# Run the bot
app.run()
