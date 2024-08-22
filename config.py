import os

from dotenv import load_dotenv

load_dotenv()

#### Load Env ####
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
MNG_ID = int(os.getenv("MCH")) # 運営チャンネルID
CWD = os.getenv("CWD")
##################

# run flag
RUNNING_FLAG = True
