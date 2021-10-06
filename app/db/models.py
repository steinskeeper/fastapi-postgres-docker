from sqlalchemy.dialects.postgresql import JSON
from .base import db, Base
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    BigInteger,
    DateTime,
)
from sqlalchemy.dialects.postgresql import ARRAY, array
from sqlalchemy.orm import relationship

import fity3
import jwt
import json
from werkzeug.security import generate_password_hash
from sqlalchemy.ext.mutable import Mutable

f3 = fity3.generator(1)


class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(255), nullable=True)
    picture = Column(String)
    bio = Column(String, default="")
    role = Column(String, default="writer")

    def __init__(self, name, email, password, picture=None, bio=None):
        self.user_id = next(f3)
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.picture = picture
        self.bio = bio

    def __repr__(self):
        return f"<User id:{self.user_id} name:{self.name}>"

    def encode_auth_token(user_id):
        """Generates the access token."""
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(
                    days=30,
                    seconds=30,
                ),
                "iat": datetime.datetime.utcnow(),
                "sub": str(user_id),
            }
            return jwt.encode(payload, "poppushpoppushpoppop", algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the access token - :param auth_token: - :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, "poppushpoppushpoppop")
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."

    def insert(self):
        db.add(self)
        db.commit()

    def update(self):
        db.commit()

    def delete_all():
        db.query(User).delete()
        db.commit()

    def format(self):
        return {
            "name": self.name,
            # "id": self.user_id,
            "email": self.email,
            "picture": self.picture,
            "bio": self.bio,
            "role": self.role,
        }
