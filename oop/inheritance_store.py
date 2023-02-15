class User:
    """A user of the store."""

    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._is_logged_in = False

    def login(self, password):
        """Log in the user."""
        if password == self._password:
            self._is_logged_in = True
            print('Login successful')
        else:
            print('Login failed')

    def show_status(self):
        """Show the user's status."""
        print(f'Name: {self._name}')
        print(f'Is logged in: {self._is_logged_in}')


customer = User('Roy', 'supersecret')

customer.login("wrongpassword")
customer.show_status()

customer.login("supersecret")
customer.show_status()


class Admin(User):
    """An admin user of the store."""

    def __init__(self, name, password, staff_id):
        super().__init__(name, password)
        self._staff_id = staff_id
        self._is_admin = True

    def show_status(self):
        """Show the admin's status."""
        super().show_status()
        print(f'Staff ID: {self._staff_id}')

    def add_product(self, product):
        """Add a product to the store."""

        if self._is_logged_in:
            print(f'{self._name} ({self._staff_id}) Adding product {product}')
        else:
            print('You must be logged in to add a product')


admin = Admin("Roy", "supersecret", 1234)
admin.show_status()
admin.login("supersecret")
admin.add_product("Socks")
