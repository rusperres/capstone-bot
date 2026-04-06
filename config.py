"""configuration module for the discord bot."""
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

discord_token = os.getenv("discord_token")

if not discord_token:
    raise valueerror("discord_token not found in environment variables. please set it in .env file.")

# bot configuration
command_prefix = "/"
database_file = "tickets.db"

import os
base_dir = os.path.dirname(os.path.abspath(__file__))
tickets_dir = os.path.join(base_dir, "tickets")
