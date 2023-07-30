# How to Add JWT Authentication in FastAPI Project?

This project demonstrates how to implement JWT (JSON Web Token) authentication in a FastAPI application. JWT is a widely used standard for securing web applications by providing a secure and stateless way of handling user authentication. This guide will walk you through setting up the project, installing the necessary dependencies, and running it using Docker and Docker Compose.

## Project Overview

The project includes the following components:

1. FastAPI: A modern, fast, web framework for building APIs with Python.

2. Pydantic: A data validation and settings management library for Python.

3. Passlib: A library for hashing passwords.

4. Jose: A library for handling JWT encoding and decoding.

5. Replit (key-value database): For storing user information.

## Features

- User signup: Allows users to create a new account by providing their email and password.
- User login: Allows users to log in with their email and password to receive access and refresh tokens.
- JWT Tokens: Generates access and refresh tokens upon successful login for subsequent authentication.
- Token Expiration: Sets expiration times for both access and refresh tokens to ensure security.
- User Details: Retrieves details of the currently logged-in user using the access token.
- Error Handling: Proper HTTPExceptions are raised for various error scenarios.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (>= 3.6)
- Docker
- Docker Compose

## How to Run the Project

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/ashishkrb7/How-to-Add-JWT-Authentication-in-FastAPI.git loginapp 
   cd loginapp
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```
   python -m pip install -r requirements.txt
   ```

4. Set the environment variables `JWT_SECRET_KEY` and `JWT_REFRESH_SECRET_KEY` with your preferred secret keys for encoding JWT tokens.

   ```
   set JWT_SECRET_KEY=your_secret_key_here
   set JWT_REFRESH_SECRET_KEY=your_refresh_secret_key_here
   ```

   Verify it using

   ```
   echo %JWT_SECRET_KEY%
   ```

   In linux use below command

   ```
   export JWT_SECRET_KEY=your_secret_key_here
   export JWT_REFRESH_SECRET_KEY=your_refresh_secret_key_here
   ```
   Verify it using

   ```
   echo $JWT_SECRET_KEY
   ```

5. Run the FastAPI application using `uvicorn`:

   ```
   uvicorn app:app --reload
   ```

6. The application will start, and you can access the API documentation (Swagger UI) at `http://localhost:8000/docs` in your browser.

7. Use the `/signup` and `/login` endpoints to create a new user and obtain JWT tokens.

8. Use the `/me` endpoint with the access token in the `Authorization` header to get user details.

## Project Structure

The project is structured as follows:


- `app`: Contains the main FastAPI application, models, schemas, and utility functions.
- `main.py`: The main entry point for the FastAPI application.
- `deps.py`: Contains the dependency function for retrieving the currently logged-in user from the access token.
- `database.py`: Contains the functions to do basic database operation in SQLite.
- `utils.py`: Contains utility functions for hashing passwords and generating JWT tokens.


   ```
   📦How-to-Add-JWT-Authentication-in-FastAPI
   ┣ 📜.dockerignore
   ┣ 📜.gitignore
   ┣ 📜app.py
   ┣ 📜database.py
   ┣ 📜deps.py
   ┣ 📜docker-compose.yml
   ┣ 📜Dockerfile
   ┣ 📜LICENSE
   ┣ 📜README.md
   ┣ 📜requirements.txt
   ┣ 📜schemas.py
   ┣ 📜server.py
   ┗ 📜utils.py
   ```

## Running with Docker and Docker Compose

1. Make sure you have Docker and Docker Compose installed.

2. Build the Docker image for the FastAPI app:

   ```
   docker-compose build
   ```

3. Start the FastAPI app with JWT authentication:

   ```
   docker-compose up -d
   ```

   The API will be available at `http://localhost:8000`.

4. To shut down the application, run:

   ```
   docker-compose down
   ```

## Contributing

We welcome contributions to improve this project! If you find any issues or want to add new features, please feel free to open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Developer Information

- Developer: Ashish Kumar
- Website: [https://ashishkrb7.github.io/](https://ashishkrb7.github.io/)
- Contact Email: :email: ashish.krb7@gmail.com

Feel free to get in touch for any collaborative work in the AI/ML and tech domain!

## Acknowledgments

This repository is deeply inspired by [this](https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/) article by Abdullah Adeel. I thank the developers and contributors of these excellent open-source article.

If you have any questions or need further assistance, please don't hesitate to reach out.

Happy coding!
