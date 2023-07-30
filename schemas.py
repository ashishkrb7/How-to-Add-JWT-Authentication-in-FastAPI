"""
This script contains Pydantic models for implementing JWT (JSON Web Token) authentication in a FastAPI application.

The models defined here represent different aspects of the authentication system:

1. TokenSchema: Schema for JWT tokens containing access_token and refresh_token attributes.

2. TokenPayload: Payload for JWT token containing sub (subject) and exp (expiration) attributes.

3. UserAuth: User authentication model representing user credentials (email and password) for login.

4. UserOut: User output model representing basic user information with id and email attributes.

5. SystemUser: An extended UserOut model for system users, which includes the password attribute.

These models are designed to work seamlessly with FastAPI to provide a secure and efficient authentication mechanism for API endpoints. They also include optional descriptions to help developers understand the purpose of each attribute.

For more details on the individual models, please refer to the docstrings and comments provided for each class and attribute.

Developer: Ashish Kumar
Website: https://ashishkrb7.github.io/
Contact Email: ashish.krb7@gmail.com
"""

from uuid import UUID

from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    """
    Schema for JWT tokens.

    Attributes:
        access_token (str): JWT access token.
        refresh_token (str): JWT refresh token.
    """

    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    """
    Payload for JWT token.

    Attributes:
        sub (str, optional): Subject of the token (default: None).
        exp (int, optional): Expiration time of the token (default: None).
    """

    sub: str = None
    exp: int = None


class UserAuth(BaseModel):
    """
    User authentication model.

    Attributes:
        email (str): User's email address.
        password (str): User's password (min length: 5, max length: 24).
    """

    email: str = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class UserOut(BaseModel):
    """
    User output model.

    Attributes:
        id (UUID): User's unique identifier.
        email (str): User's email address.
    """

    id: UUID
    email: str


class SystemUser(UserOut):
    """
    Extended UserOut model for system users.

    Attributes:
        password (str): User's password.
    """

    password: str
