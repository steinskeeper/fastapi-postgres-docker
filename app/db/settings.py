import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv("DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST_ADDRESS")
DB_NAME = os.getenv("DB_NAME")

