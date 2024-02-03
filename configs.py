# (c) @JAsuran2p0

import os


class Config(object):
	API_ID = 1923471
	API_HASH = "fcdc178451cd234e63faefd38895c991"

	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6885403506:AAEC0alu3bCjcCgzIMGqk6rG7540vmCkqP0")
        #BOT_USERNAME = os.environ.get("BOT_USERNAME", "AdultOnly18_Bot")
	BOT_USERNAME = "AdultOnly18_Bot"
        LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002107895168"))
        UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002138948839")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002107895168")) #Adult
	
	#BOT_TOKEN = "6288959553:AAFdAjugCCau_-SluJLU1CQiOwyYjFvWYRU" #ShareMoviesQLBot
	#BOT_TOKEN = "5925688295:AAE3mRUwnJsHdBo5TVTCibHJP--akCRU4jE" #Tamilan_Rocks1_Bot
	#BOT_TOKEN = "6898447547:AAFj3fAep2W2O69lilL3jv-TNluMJE9EnyI" #QL_Movie_Links_Bot
	
	#BOT_USERNAME = "ShareMoviesQLBot"
	#BOT_USERNAME = "Tamilan_Rocks1_Bot"
	#BOT_USERNAME = "QL_Movie_Links_Bot"
	
	#DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001624572720")) #ShareMoviesQLBot
	#DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001884285982")) #Tamilan_Rocks1_Bot
	 #DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002087036746")) #QL_Movie_Links_Bot
	
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1109543851"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://leecher:leecher@cluster0.606mkpi.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	
	#LOG_CHANNEL = "-1001624572720" #ShareMoviesQLBot
	#LOG_CHANNEL = "-1002087036746"  #QL_Movie_Links_Bot
	#LOG_CHANNEL = "-1001884285982"  #Tamilan_Rocks1_Bot
	
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

👥 **Support Group:** [Catchme](https://t.me/Quality_LinksZ)

📢 **Updates Channel:** [Quality LinkS](https://t.me/Quality_LinksZ)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** 

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
