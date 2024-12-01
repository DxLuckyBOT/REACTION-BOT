from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        f"𝐇𝐞𝐥𝐥𝐨 𝐈 𝐀𝐦 𝐃𝐱๛𝐋𝐔𝐂𝐊𝐘 𝐎𝐖𝐍𝐄𝐑 {message.from_user.first_name}! 👋\n\n"
        "I'm your Reaction Bot! I'll react to every message in groups, channels, and private chats with a 👍 emoji.\n\n"
        "Add me to your group or channel and watch me in action! 🚀\n\n"
        "**You can make your bot by /clone😁**"
    )
    
