from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://intigam:1234@localhost/intigam"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

SECRET_KEY = "X_aebhfjvdAFENKRV-72486aenvjAAAA_____BB"
ALGORITHM = "HS256"

class Settings:
    SECRET_KEY = SECRET_KEY
    ALGORITHM = ALGORITHM
    DATABASE_URL = DATABASE_URL

settings = Settings()
