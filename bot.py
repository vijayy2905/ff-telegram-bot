import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def send_autolike(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    
    player = args[0] if len(args) > 0 else "Max!!"
    uid = args[1] if len(args) > 1 else "865530641"
    region = args[2] if len(args) > 2 else "ind"
    before = args[3] if len(args) > 3 else "24121"
    after = args[4] if len(args) > 4 else "24308"
    likes_given = args[5] if len(args) > 5 else "187"
    total_likes = args[6] if len(args) > 6 else "742"
    progress = args[7] if len(args) > 7 else "12/12"

    caption_text = (
        "🔴 **AUTOLIKE SUCCESSFUL**\n\n"
        "╭━━━━━━━━━\" 𝟗𝟗\n"
        "┆\n"
        f"┆ 👤 **Player:** {player}\n"
        f"┆ 🛡️ **UID:** `{uid}`\n"
        f"┆ 📍 **Region:** {region}\n"
        f"┆ 📊 **Before:** {before}\n"
        f"┆ 📈 **After:** {after}\n"
        f"┆ 🎁 **Likes Given:** {likes_given}\n"
        f"┆ 📊 **Total Likes:** {total_likes}\n"
        "┆\n"
        "╰━━━━━━━━━\"\n\n"
        f"⚙️ **Progress:** {progress}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👑 BUY LIKES", url="https://t.me/your_admin_or_channel")]
    ])

    image_filename = "banner.PNG" if os.path.exists("banner.PNG") else "banner.png"

    if os.path.exists(image_filename):
        with open(image_filename, "rb") as photo_file:
            await update.message.reply_photo(
                photo=photo_file,
                caption=caption_text,
                parse_mode="Markdown",
                reply_markup=keyboard
            )
    else:
        await update.message.reply_text(
            text=caption_text,
            parse_mode="Markdown",
            reply_markup=keyboard
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("autolike", send_autolike))
    print("Bot is live on Render...")
    app.run_polling()

if __name__ == "__main__":
    main()
