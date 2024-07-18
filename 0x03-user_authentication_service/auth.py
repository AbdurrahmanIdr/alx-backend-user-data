#!/usr/bin/env python3
""" Hash password """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Return a salted, hashed password, which is a byte string """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check if password is valid """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


def _generate_uuid() -> str:
    """ Generate a UUID """
    return str(uuid.uuid4())


