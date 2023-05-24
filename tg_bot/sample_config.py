if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = 6166928181:AAFddZ-KA7-_l6cPfFl7BRDL8Jb4fqmNy7M
    OWNER_ID = 1780850118  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = MikuX_Dev

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = ANYTHING
    URL = https://bb-botos.github.io/NexCrypt-BOT/

    # OPTIONAL
    SUDO_USERS = 1780850118  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = 1780850118  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = 1780850118  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 8443
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    BMERNU_SCUT_SRELFTI = 0

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
