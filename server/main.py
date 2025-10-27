from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid, bcrypt

app = FastAPI()

DATABASE_URL: str = (
    "postgresql://postgres:postgres1290!@localhost:5432/Flutter Spotify Clone"
)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = SessionLocal()

Base = declarative_base()


class CreateUser(BaseModel):
    name: str
    email: str
    password: str


class User(Base):
    __tablename__ = "users"

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)


@app.post("/signup")
def user_signup(user: CreateUser):
    user_databse = database.query(User).filter(User.email == user.email).first()

    if user_databse:
        raise HTTPException(400, "User with the same email already exists!")

    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_databse = User(
        id=str(uuid.uuid4()), name=user.name, email=user.email, password=hashed_password
    )
    database.add(user_databse)
    database.commit()
    database.refresh(user_databse)

    return user_databse


Base.metadata.create_all(engine)
