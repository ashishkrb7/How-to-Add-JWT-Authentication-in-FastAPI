"""
FastAPI Authentication Endpoints

This script contains the FastAPI endpoints responsible for user authentication and user-related actions. It includes the following endpoints:

1. /signup:
   - Method: POST
   - Summary: Create a new user.
   - Description: This endpoint allows users to sign up by providing their email and password. It checks if the user already exists in the database and raises an HTTPException if the user already has an account. If the user is new, their data is hashed, and a unique identifier (UUID) is generated for the user. The user's data is then saved to the database.
   - Response Model: UserOut (User output model containing user's email and unique identifier).

2. /login:
   - Method: POST
   - Summary: Create access and refresh tokens for the user.
   - Description: This endpoint allows users to log in using their email and password. It verifies the user's credentials by checking the hashed password against the one stored in the database. If the credentials are valid, the endpoint generates and returns both an access token and a refresh token for the user. These tokens can be used for authentication in subsequent requests.
   - Response Model: TokenSchema (Schema for JWT tokens containing access_token and refresh_token attributes).

3. /me:
   - Method: GET
   - Summary: Get details of the currently logged-in user.
   - Description: This endpoint requires a valid JWT access token to be provided in the Authorization header. It uses the get_current_user dependency (SystemUser) to extract and validate the user's information from the token payload. If the token is valid and the user is found in the database, their details are returned in the response.
   - Response Model: UserOut (User output model containing user's email and unique identifier).

Developer: Ashish Kumar
Website: https://ashishkrb7.github.io/
Contact Email: ashish.krb7@gmail.com
"""

from uuid import uuid4

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from replit import db

from app.schemas import SystemUser, TokenSchema, UserAuth, UserOut
from deps import get_current_user
from utils import (
    create_access_token,
    create_refresh_token,
    get_hashed_password,
    verify_password,
)

app = FastAPI()


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def docs():
    """
    Redirect to the API documentation (Swagger UI).
    """
    return RedirectResponse(url="/docs")


@app.post("/signup", summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    """
    Endpoint to create a new user.

    Args:
        data (UserAuth): User authentication model containing user's email and password.

    Returns:
        dict: The user data containing email and unique identifier (UUID).

    Raises:
        HTTPException: If a user with the same email already exists in the database (status code 400).
    """
    # querying the database to check if the user already exists
    user = db.get(data.email, None)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    user = {
        "email": data.email,
        "password": get_hashed_password(data.password),
        "id": str(uuid4()),
    }
    db[data.email] = user  # saving user data to the database
    return user


@app.post(
    "/login",
    summary="Create access and refresh tokens for user",
    response_model=TokenSchema,
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint to create access and refresh tokens for a user upon successful login.

    Args:
        form_data (OAuth2PasswordRequestForm, optional): OAuth2 password request form containing username and password.

    Returns:
        dict: Dictionary containing access_token and refresh_token as keys.

    Raises:
        HTTPException: If the provided email or password is incorrect (status code 400).
    """
    user = db.get(form_data.username, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    hashed_pass = user["password"]
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    return {
        "access_token": create_access_token(user["email"]),
        "refresh_token": create_refresh_token(user["email"]),
    }


@app.get(
    "/me", summary="Get details of currently logged in user", response_model=UserOut
)
async def get_me(user: SystemUser = Depends(get_current_user)):
    """
    Endpoint to get details of the currently logged-in user.

    Args:
        user (SystemUser, optional): SystemUser instance representing the currently authenticated user.

    Returns:
        dict: User data containing email and unique identifier (UUID).

    Raises:
        HTTPException: If the user is not found in the database (status code 404).
    """
    return user
