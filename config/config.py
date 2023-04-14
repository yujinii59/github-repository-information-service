import os
from dotenv import load_dotenv

# load .env
load_dotenv()

# get github token
TOKEN = os.environ.get("github_token", '')
