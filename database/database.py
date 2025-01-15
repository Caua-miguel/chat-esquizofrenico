import psycopg  # noqa: F401
import os  # noqa: F401
from dotenv import load_dotenv

load_dotenv()

db = psycopg.connect(os.getenv('DATABASE_URI'))
cursor = db.cursor()


