class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_to_add_button()
        self.connect_to_generate_password_button()

    def retrieve_and_save_user_data(self) -> None:
        website, email_username, password = self.view.get_user_input()
        if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
            self.view.show_messagebox(message="Please fill all fields", type_of_messagebox="error")
        else:
            is_yes = self.view.show_messagebox(message=f"Website link: {website}\nEmail/Username: {email_username}\nPassword: {password}", type_of_messagebox="confirmation")
            if is_yes:
                self.model.save_data_to_file(
                    website=website,
                    email_username=email_username,
                    password=password
                )
                self.view.init_inputs()
        self.view.focus_window()
        self.view.focus_cursor()

    def connect_to_add_button(self) -> None:
        self.view.add_to_file(self.retrieve_and_save_user_data)

    def generate_and_show_password(self) -> None:
        num = self.view.get_number_of_characters()
        if num is not None:
            password = self.model.generate_password(num)
            self.view.set_password(password)

    def connect_to_generate_password_button(self) -> None:
        self.view.generate_password_click(command=self.generate_and_show_password)
