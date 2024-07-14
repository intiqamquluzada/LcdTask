from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DEBUG = True


if not DEBUG:
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{intigam}:{1234}@localhost:3306/{lcd}"
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()