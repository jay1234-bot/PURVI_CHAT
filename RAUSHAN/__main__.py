from flask import Flask
import threading
import asyncio
from RAUSHAN import LOGGER, AMBOT

app = Flask(__name__)

# Flask route
@app.route("/")
def home():
    return "Bot is running"

# Flask thread function
def run_flask():
    app.run(host="0.0.0.0", port=8000)

# Bot async function
async def run_bot():
    LOGGER.info("The PURVI CHAT BOT Started.")
    bot = AMBOT()
    await bot.start()
    await idle()  # Keeps the bot running

# Main thread
if __name__ == "__main__":
    from pyrogram import idle  # imported here to avoid early call

    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run bot in main thread
    asyncio.run(run_bot())
