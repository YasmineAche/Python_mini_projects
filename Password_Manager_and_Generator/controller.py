class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_to_add_button()
        self.connect_to_generate_password_button()
        self.connect_to_search_button()

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
        self.view.generate_password_clicked(command=self.generate_and_show_password)

    def search_and_display_data(self) -> None:
        website = self.view.get_researched_website_name()
        if len(website) == 0:
            self.view.show_messagebox(message="Please enter a valid website", type_of_messagebox="error")
            self.view.focus_window()
            self.view.focus_cursor()
        else:
            found_data = self.model.search_for_data(website)
            if len(found_data) > 0:
                self.view.display_found_data(found_data)
            else:
                self.view.show_messagebox(message="No data found for the given website", type_of_messagebox="information")
                self.view.focus_window()
                self.view.focus_cursor()

    def connect_to_search_button(self) -> None:
        self.view.search_data_clicked(command=self.search_and_display_data)
