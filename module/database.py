
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

with open('./conf/config.json', 'r') as f:
    config = json.load(f)

dbUrl = config['DB_URL']
dbUser = config['DB_USER']
dbPasswd = config['DB_PASSWD']
engine = create_engine('postgresql+psycopg2://'+dbUser+":"+dbPasswd+"@"+dbUrl, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(engine)
