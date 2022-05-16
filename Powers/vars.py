from os import getcwd


from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])



class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default=None))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-100))
    DEV_USERS = [int(i) for i in config("DEV_USERS", default="1432756163 1344569458 1355478165 1789859817 1777340882").split(" ")]
    SUDO_USERS = [int(i) for i in config("SUDO_USERS", default="1432756163 1344569458 1355478165 1789859817 1777340882").split(" ")]
    WHITELIST_USERS = [int(i) for i in config("WHITELIST_USERS", default="1432756163 1344569458 1355478165 1789859817 1777340882").split(" ")]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="gojo_satarou")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_update")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_updates")
    VERSION = config("VERSION", default="v2.0")
    WORKERS = int(config("WORKERS", default=16))
    ARQ_API_URL = config("ARQ_API_URL", default="https://arq.hamker.in")
    ARQ_API_KEY = config("ARQ_API_KEY", default=None)
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "YOUR BOT_TOKEN"
    API_ID = 12345  # Your APP_ID from Telegram
    API_HASH = "YOUR API HASH"  # Your APP_HASH from Telegram
    OWNER_ID = 1344569458  # Your telegram user id
    MESSAGE_DUMP = -100  # Your Private Group ID for logs
    DEV_USERS = []
    SUDO_USERS = []
    WHITELIST_USERS = []
    DB_URI = "postgres://username:password@postgresdb:5432/database_name"
    DB_NAME = "gojo_satarou"
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "SUPPORT_GROUP"
    SUPPORT_CHANNEL = "SUPPORT_CHANNEL"
    VERSION = "VERSION"
    WORKERS = 8
    ARQ_API_URL = "ARQ API url here"
    ARQ_API_KEY = "ARQ API key here"
