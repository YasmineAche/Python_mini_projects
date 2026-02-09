import os
import string
from random import choice

class Model:
    def __init__(self):
        self.data_file_path = "user_data.txt"
        self.characters = f"{string.ascii_letters}{string.digits}{string.punctuation}"
        self.create_data_file()

    def create_data_file(self) -> None:
        if not os.path.exists(self.data_file_path):
            with open(self.data_file_path, "w") as file:
                file.write(f"Website | Email/Username | Password\n{"-"*35}\n")

    def save_data_to_file(self, website:str, email_username:str, password:str) -> None:
        with open(self.data_file_path, "a") as file:
            file.write(f"{website} | {email_username} | {password}\n")

    def generate_password(self, number_of_characters:int) -> str:
        password = "".join(choice(self.characters) for i in range(number_of_characters))
        return password
