from configparser import ConfigParser
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


path = Path(__file__).parent.parent.joinpath('config.ini')
parser = ConfigParser()
parser.read(path)

user = parser.get('DB', 'USER')
password = parser.get('DB', 'PASSWORD')
domain = parser.get('DB', 'DOMAIN')
port = parser.get('DB', 'PORT')
db = parser.get('DB', 'DB_NAME')

URI = f'postgresql://{user}:{password}@{domain}:{port}/{db}'

engine = create_engine(URI, echo=False, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()
