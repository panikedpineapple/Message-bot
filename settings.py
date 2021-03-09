import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "!"

# The bot token. Keep this secret!
BOT_TOKEN = "ODE4NDcwNjkzNDI2OTU0Mjcx.YEYiOw.RGKdynuguh4gAkWWpMJ2YPtcKhY"

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = COMMAND_PREFIX + "commands"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

ALLOWED_CHANNELS = [818470383513763853]

USER_WATCHLIST = [225911806034575361]