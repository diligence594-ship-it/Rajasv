import os
from flask import Flask
from threading import Thread
from pyrogram import idle
from Extractor import app
from Extractor.modules import ALL_MODULES
from cleanup import start_cleanup_scheduler


# --------------------------------------------------
# Flask
# --------------------------------------------------

web = Flask(__name__)


@web.route("/")
def home():
    return "Bot is running!"


def run_flask():
    port = int(os.getenv("PORT", 8080))
    web.run(
        host="0.0.0.0",
        port=port
    )


Thread(
    target=run_flask,
    daemon=True
).start()


# --------------------------------------------------
# Cleanup scheduler
# --------------------------------------------------

try:
    start_cleanup_scheduler()
    print("Cleanup scheduler started.")
except Exception as e:
    print(f"Cleanup scheduler error: {e}")


# --------------------------------------------------
# Load modules
# --------------------------------------------------

for module in ALL_MODULES:
    try:
        __import__("Extractor.modules." + module)
        print(f"Loaded module: {module}")
    except Exception as e:
        print(f"Failed to load {module}: {e}")


# --------------------------------------------------
# Keep bot alive
# --------------------------------------------------

if __name__ == "__main__":
    print("Bot is already started by Extractor.")

    try:
        idle()
    except Exception as e:
        print(f"Bot stopped: {e}")
    finally:
        print("Application stopped.")

Thread(
    target=run_flask,
    daemon=True
).start()


# --------------------------------------------------
# Load all bot modules
# --------------------------------------------------
for module in ALL_MODULES:
    try:
        __import__("Extractor.modules." + module)
        print(f"Loaded module: {module}")
    except Exception as e:
        print(f"Failed to load {module}: {e}")


# --------------------------------------------------
# Start bot
# --------------------------------------------------
if __name__ == "__main__":
    print("Starting Telegram bot...")

    try:
        app.start()
        print("Bot started successfully!")

        idle()

    except Exception as e:
        print(f"Bot error: {e}")

    finally:
        try:
            app.stop()
        except Exception:
            pass
