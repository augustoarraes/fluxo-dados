
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
import dotenv, os


dotenv.load_dotenv(".env")

url = URL.create(
    drivername=os.environ["DB_DRIVE"],
    username=os.environ["DB_USERNAME"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    database=os.environ["DB_DATABASE"],
    port=os.environ["DB_PORT"]
)

print(url)
engine = create_engine(url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(bind=engine)


def new_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()