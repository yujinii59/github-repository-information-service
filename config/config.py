import os
from dotenv import load_dotenv

# load .env
load_dotenv()
TOKEN = os.environ.get("github_token", '')
