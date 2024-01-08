from pyrogram import Client, filters
from sh_bots.font_list import Font


@app.on_message(filters.command("font"))
async def stylize_text(client, message):
    text_to_stylize = message.text.split(" ", 1)[1]  
    stylized_text = Font.SH(text_to_stylize)  

    await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴛᴇxᴛ: <code>{stylized_text}</code>")

