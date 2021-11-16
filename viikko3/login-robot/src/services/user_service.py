from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not re.match(r"[a-zA-Z]{3,}", username):
            raise UserInputError("Username must contain [a-z] and be atleast 3 characters long")

        if not re.match(r"^(?=.*[0-9])(?=.*[a-zA-Z])(?=\S+$).{8,}$", password):
            raise UserInputError("Password must contain both characters and numbers and be atleast 8 characters long")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already exists")