#Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
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

print("Bot Started! 🦋 © t.me/Sunrises_24")

# Function to handle /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Welcome! Send me an image and choose an action.\n"
        "Available commands:\n"
        "/grayscale - Convert to Grayscale\n"
        "/enhance - Enhance the image\n"
        "/changebg - Change Background\n"
        "/blurportrait - Blur to Portrait\n"
        "/changeshirtcolor - Change Shirt Color"
    )

# Function to convert image to grayscale
def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    return grayscale_image

# Function to enhance an image
def enhance_image(image_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(1.5)  # Adjust enhancement factor as needed
    return enhanced_image

# Function to change background (replace with solid color)
def change_background(image_path, color=(255, 255, 255)):
    image = Image.open(image_path)
    width, height = image.size
    background = Image.new("RGB", (width, height), color)
    background.paste(image, (0, 0), image)
    return background

# Function to blur the background in a portrait-style photo
def blur_portrait(image_path):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=10))
    return blurred_image

# Function to change shirt color
def change_shirt_color(image_path, new_color=(255, 0, 0)):
    image = Image.open(image_path)
    # Assuming the shirt is red, changing the color to a new_color
    image = ImageOps.colorize(image.convert('L'), black="black", white=new_color)
    return image

# Function to handle /grayscale command
@app.on_message(filters.command("grayscale"))
async def grayscale_command(client, message):
    photo = await message.reply_to_message.download()
    grayscale_image = convert_to_grayscale(photo)
    grayscale_image_path = "grayscale_" + str(message.chat.id) + ".png"
    grayscale_image.save(grayscale_image_path)
    await message.reply_photo(
        photo=grayscale_image_path,
        caption="Grayscale filter applied!"
    )
    os.remove(grayscale_image_path)

# Function to handle /enhance command
@app.on_message(filters.command("enhance"))
async def enhance_command(client, message):
    photo = await message.reply_to_message.download()
    enhanced_image = enhance_image(photo)
    enhanced_image_path = "enhanced_" + str(message.chat.id) + ".png"
    enhanced_image.save(enhanced_image_path)
    await message.reply_photo(
        photo=enhanced_image_path,
        caption="Enhanced image!"
    )
    os.remove(enhanced_image_path)

# Function to handle /changebg command
@app.on_message(filters.command("changebg"))
async def changebg_command(client, message):
    photo = await message.reply_to_message.download()
    changed_bg_image = change_background(photo)
    changed_bg_image_path = "changed_bg_" + str(message.chat.id) + ".png"
    changed_bg_image.save(changed_bg_image_path)
    await message.reply_photo(
        photo=changed_bg_image_path,
        caption="Background changed!"
    )
    os.remove(changed_bg_image_path)

# Function to handle /blurportrait command
@app.on_message(filters.command("blurportrait"))
async def blurportrait_command(client, message):
    photo = await message.reply_to_message.download()

    blurred_image = blur_portrait(photo)
    blurred_image_path = "blurred_" + str(message.chat.id) + ".png"
    blurred_image.save(blurred_image_path)
    await message.reply_photo(
        photo=blurred_image_path,
        caption="Background blurred for portrait effect!"
    )
    os.remove(blurred_image_path)

# Function to handle /changeshirtcolor command
@app.on_message(filters.command("changeshirtcolor"))
async def changeshirtcolor_command(client, message):
    photo = await message.reply_to_message.download()
    new_shirt_color = change_shirt_color(photo)
    new_shirt_color_path = "new_shirt_color_" + str(message.chat.id) + ".png"
    new_shirt_color.save(new_shirt_color_path)
    await message.reply_photo(
        photo=new_shirt_color_path,
        caption="Shirt color changed!"
    )
    os.remove(new_shirt_color_path)

# Run the bot
app.run()
