import os
import string
from random import choice

DATA_FILE_PATH = "user_data.txt"

class Model:
    def __init__(self):
        self.characters = f"{string.ascii_letters}{string.digits}{string.punctuation}"
        self.create_data_file()

    @staticmethod
    def create_data_file() -> None:
        if not os.path.exists(DATA_FILE_PATH):
            with open(DATA_FILE_PATH, "w") as file:
                file.write(f"Website | Email/Username | Password\n{"-"*35}\n")

    @staticmethod
    def save_data_to_file(website:str, email_username:str, password:str) -> None:
        with open(DATA_FILE_PATH, "a") as file:
            file.write(f"{website} | {email_username} | {password}\n")

    def generate_password(self, number_of_characters:int) -> str:
        password = "".join(choice(self.characters) for i in range(number_of_characters))
        return password
