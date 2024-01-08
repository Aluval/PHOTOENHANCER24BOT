#Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
from pyrogram import Client, filters
import numpy as np

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

# Function to convert blur to HDR-style photo (placeholder)
def convert_to_hdr(image_path):
    image = Image.open(image_path)

    # Convert the image to a numpy array
    image_array = np.array(image)

    # Apply a Gaussian blur to create a base for the HDR effect
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=10))

    # Convert blurred image to numpy array
    blurred_array = np.array(blurred_image)

    # Calculate the difference between original and blurred image
    difference = image_array - blurred_array

    # Enhance the difference to exaggerate the dynamic range
    enhanced_difference = Image.fromarray(difference).filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

    # Add the enhanced difference back to the original image
    hdr_image = ImageEnhance.Contrast(image).enhance(2.0)  # Enhancing contrast for HDR effect
    hdr_image = Image.blend(hdr_image, enhanced_difference, alpha=0.7)  # Adjust alpha for blending strength

    return hdr_image

# Function to change dress color (placeholder)
def change_dress_color(image_path, new_color=(255, 0, 0)):
    # Open the image
    image = Image.open(image_path)
    
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Define the old color you want to replace (e.g., red)
    old_color = np.array([255, 0, 0])  # Red color in RGB
    
    # Define the threshold for color replacement (adjust as needed)
    threshold = 100
    
    # Create a mask for pixels within the threshold of the old color
    mask = np.abs(image_array - old_color) < threshold
    
    # Replace pixels within the mask with the new color
    image_array[mask] = new_color
    
    # Create a new image from the modified array
    modified_image = Image.fromarray(image_array)
    
    return modified_image

#Function to handle /grayscale command
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
    hdr_image = convert_to_hdr(photo)
    hdr_image_path = "hdr_" + str(message.chat.id) + ".png"
    hdr_image.save(hdr_image_path)
    await message.reply_photo(
        photo=hdr_image_path,
        caption="HDR-style image!"
    )
    os.remove(hdr_image_path)

# Function to handle /changedresscolor command
@app.on_message(filters.command("changedresscolor"))
async def changedresscolor_command(client, message):
    photo = await message.reply_to_message.download()
    change_dress_color(photo)
    # Implement logic to change dress color and reply with the result

# Running the bot
app.run()
