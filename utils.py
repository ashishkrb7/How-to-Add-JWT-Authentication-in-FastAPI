"""
JWT (JSON Web Token) Utility Functions

This module contains utility functions for handling JWT (JSON Web Token) authentication in a FastAPI application. It includes functions for generating hashed passwords, verifying passwords, and creating both access and refresh tokens.

The JWT tokens are used for authenticating users in the application. The tokens are encoded using a specified algorithm and secret keys, and they have expiration times to ensure security.

Functions:
    - get_hashed_password: Hashes a password using the bcrypt algorithm.
    - verify_password: Verifies if a provided password matches the hashed password.
    - create_access_token: Creates an access token with a specified expiration time for a given subject.
    - create_refresh_token: Creates a refresh token with a specified expiration time for a given subject.

Constants:
    - ACCESS_TOKEN_EXPIRE_MINUTES: The expiration time for access tokens in minutes (default: 30 minutes).
    - REFRESH_TOKEN_EXPIRE_MINUTES: The expiration time for refresh tokens in minutes (default: 7 days).
    - ALGORITHM: The algorithm used for encoding the JWT tokens (default: HS256).
    - JWT_SECRET_KEY: The secret key used for encoding access tokens. Should be kept secret.
    - JWT_REFRESH_SECRET_KEY: The secret key used for encoding refresh tokens. Should be kept secret.

Developer: Ashish Kumar

Website: https://ashishkrb7.github.io/

Contact Email: ashish.krb7@gmail.com
"""

import os
from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

# Expiration times for tokens
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

# JWT settings
ALGORITHM = "HS256"
JWT_SECRET_KEY = "ashish"  # os.environ["JWT_SECRET_KEY"]  # should be kept secret
JWT_REFRESH_SECRET_KEY = (
    "ashish"  # os.environ["JWT_REFRESH_SECRET_KEY"]  # should be kept secret
)

# CryptContext for password hashing
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    """
    Hashes the provided password using the bcrypt algorithm.

    Args:
        password (str): The plain-text password to be hashed.

    Returns:
        str: The hashed password.
    """
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    """
    Verifies if the provided password matches the hashed password.

    Args:
        password (str): The plain-text password to be verified.
        hashed_pass (str): The hashed password to be compared with.

    Returns:
        bool: True if the password is verified, False otherwise.
    """
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """
    Creates an access token for the specified subject with an optional expiration time.

    Args:
        subject (Union[str, Any]): The subject of the token, typically representing the user.
        expires_delta (int, optional): The duration in seconds after which the token will expire (default: 30 minutes).

    Returns:
        str: The encoded access token.
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """
    Creates a refresh token for the specified subject with an optional expiration time.

    Args:
        subject (Union[str, Any]): The subject of the token, typically representing the user.
        expires_delta (int, optional): The duration in seconds after which the token will expire (default: 7 days).

    Returns:
        str: The encoded refresh token.
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=REFRESH_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
