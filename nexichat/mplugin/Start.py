from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

@Client.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        f"𝐇𝐞𝐥𝐥𝐨 𝐈 𝐚𝐦 𝐃𝐱๛𝐋𝐮𝐜𝐤𝐲\n {message.from_user.first_name}! 👋\n\n"
        "I'm your Reaction Bot! [❤️ Owner ❤️](https://t.me/DX_LUCKY) !I'll react to every message in groups, channels, and private chats with a 👍 emoji.\n\n"
        "Add me to your group or channel and watch me in action! 🚀\n\n"
        "**You can make your bot by /clone😁**"
    )
