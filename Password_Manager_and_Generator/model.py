import os
import string
from random import choice
import json

DATA_FILE_PATH = "user_data.json"

class Model:
    def __init__(self):
        self.characters = f"{string.ascii_letters}{string.digits}{string.punctuation}"
        self.create_data_file()

    @staticmethod
    def create_data_file() -> None:
        if not os.path.exists(DATA_FILE_PATH):
            with open(DATA_FILE_PATH, "w") as file:
                json.dump({}, file)

    @staticmethod
    def save_data_to_file(website: str, email_username: str, password: str) -> None:
        new_data = {
            website: {
                "email/username": email_username,
                "password": password
            }
        }
        with open(DATA_FILE_PATH, "r") as file:
            data = json.load(file)
            data.update(new_data)

        with open(DATA_FILE_PATH, "w") as file:
            json.dump(obj=data, fp=file, indent=4)

    def generate_password(self, number_of_characters: int) -> str:
        password = "".join(choice(self.characters) for _ in range(number_of_characters))
        return password
