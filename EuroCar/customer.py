from shop import Store
class Customer:
    def __init__(self) -> None:
        self.first_name = ""
        self.last_name = ""

    def get_user_info(self):
        self.first_name = str(input("Enter your first name\n> "))
        self.last_name = str(input("Enter your last name\n> "))
        Store.greeting(self)
