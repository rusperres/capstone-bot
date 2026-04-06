"""configuration module for the discord bot."""
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN not found in environment variables.")

command_prefix = "/"
database_file = "tickets.db"

base_dir = os.path.dirname(os.path.abspath(__file__))
TICKETS_DIR = os.path.join(base_dir, "tickets")
