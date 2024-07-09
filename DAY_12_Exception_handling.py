'''ATM Withdrawal: Write a function that simulates an ATM withdrawal. 
The function should check if the account balance is sufficient for the withdrawal amount 
and raise an exception if not. Handle scenarios where the input
withdrawal amount is not a number or is negative.'''
class InsufficientBalanceError(Exception):
    pass

class InvalidWithdrawalAmountError(Exception):
    pass

def atm_withdrawal(account_balance, withdrawal_amount):
    """
    Simulates an ATM withdrawal.

    Args:
        account_balance (float): The current account balance.
        withdrawal_amount (float): The amount to withdraw.

    Returns:
        float: The new account balance after withdrawal.

    Raises:
        InsufficientBalanceError: If the account balance is insufficient.
        InvalidWithdrawalAmountError: If the withdrawal amount is not a number or is negative.
    """
    try:
        withdrawal_amount = float(withdrawal_amount)
    except ValueError:
        raise InvalidWithdrawalAmountError("Withdrawal amount must be a number.")

    if withdrawal_amount < 0:
        raise InvalidWithdrawalAmountError("Withdrawal amount cannot be negative.")

    if withdrawal_amount > account_balance:
        raise InsufficientBalanceError("Insufficient balance in account.")

    new_balance = account_balance - withdrawal_amount
    return new_balance

# Example usage:
account_balance = 1000
while True:
    try:
        withdrawal_amount = input("Enter withdrawal amount: ")
        new_balance = atm_withdrawal(account_balance, withdrawal_amount)
        print(f"Withdrawal successful. New balance: {new_balance}")
        break
    except InsufficientBalanceError as e:
        print(e)
    except InvalidWithdrawalAmountError as e:
        print(e)


'''User Login System: Create a function that simulates a user login system. 
It should raise an exception if the username or password is incorrect and handle 
cases where the input values are empty strings.'''
class InvalidUsernameError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

def login_system(username, password, valid_username, valid_password):
    """
    Simulates a user login system.

    Args:
        username (str): The username entered by the user.
        password (str): The password entered by the user.
        valid_username (str): The valid username.
        valid_password (str): The valid password.

    Returns:
        str: A success message if the login is successful.

    Raises:
        InvalidUsernameError: If the username is incorrect or empty.
        InvalidPasswordError: If the password is incorrect or empty.
    """
    if not username:
        raise InvalidUsernameError("Username cannot be empty.")
    if not password:
        raise InvalidPasswordError("Password cannot be empty.")

    if username != valid_username:
        raise InvalidUsernameError("Invalid username.")
    if password != valid_password:
        raise InvalidPasswordError("Invalid password.")

    return "Login successful!"

# Example usage:
valid_username = "admin"
valid_password = "password"

while True:
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        print(login_system(username, password, valid_username, valid_password))
        break
    except InvalidUsernameError as e:
        print(e)
    except InvalidPasswordError as e:
        print(e)


'''Online Shopping Cart: Write a function that adds items to an online shopping cart. 
Handle scenarios where the item is out of stock, the item ID is invalid, or the quantity 
requested is more than the available stock.'''
class ItemOutOfStockError(Exception):
    pass

class InvalidItemIDError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item_id, quantity, inventory):
        """
        Adds an item to the shopping cart.

        Args:
            item_id (str): The ID of the item to add.
            quantity (int): The quantity of the item to add.
            inventory (dict): A dictionary of items with their available stock.

        Returns:
            None

        Raises:
            ItemOutOfStockError: If the item is out of stock.
            InvalidItemIDError: If the item ID is invalid.
            InsufficientStockError: If the quantity requested is more than the available stock.
        """
        if item_id not in inventory:
            raise InvalidItemIDError(f"Item ID '{item_id}' is invalid.")

        if inventory[item_id] == 0:
            raise ItemOutOfStockError(f"Item '{item_id}' is out of stock.")

        if quantity > inventory[item_id]:
            raise InsufficientStockError(f"Only {inventory[item_id]} items available for '{item_id}'.")

        if item_id in self.cart:
            self.cart[item_id] += quantity
        else:
            self.cart[item_id] = quantity

        inventory[item_id] -= quantity

    def view_cart(self):
        """
        Displays the items in the shopping cart.

        Returns:
            str: A string representation of the shopping cart.
        """
        cart_str = "Shopping Cart:\n"
        for item, quantity in self.cart.items():
            cart_str += f"  {item}: {quantity}\n"
        return cart_str

# Example usage:
inventory = {
    "item1": 10,
    "item2": 20,
    "item3": 0,  # out of stock
}

cart = ShoppingCart()

while True:
    try:
        item_id = input("Enter item ID: ")
        quantity = int(input("Enter quantity: "))
        cart.add_item(item_id, quantity, inventory)
        print(cart.view_cart())
    except ItemOutOfStockError as e:
        print(e)
    except InvalidItemIDError as e:
        print(e)
    except InsufficientStockError as e:
        print(e)



'''Temperature Conversion: Implement a function that converts 
temperatures between Fahrenheit and Celsius. Raise an exception if the input 
is not a number and handle this error gracefully.'''
class InvalidInputError(Exception):
    pass

def convert_temperature(temp, from_unit, to_unit):
    """
    Converts a temperature from one unit to another.

    Args:
        temp (str): The temperature value to convert.
        from_unit (str): The unit of the input temperature (either 'F' or 'C').
        to_unit (str): The unit to convert to (either 'F' or 'C').

    Returns:
        float: The converted temperature value.

    Raises:
        InvalidInputError: If the input temperature is not a number.
    """
    try:
        temp = float(temp)
    except ValueError:
        raise InvalidInputError("Invalid input. Temperature must be a number.")

    if from_unit == 'F' and to_unit == 'C':
        return (temp - 32) * 5.0/9.0
    elif from_unit == 'C' and to_unit == 'F':
        return temp * 9.0/5.0 + 32
    else:
        raise InvalidInputError("Invalid unit. Unit must be either 'F' or 'C'.")

def main():
    while True:
        try:
            temp = input("Enter temperature: ")
            from_unit = input("Enter unit (F or C): ")
            to_unit = input("Enter unit to convert to (F or C): ")
            result = convert_temperature(temp, from_unit, to_unit)
            print(f"{temp} {from_unit} is equal to {result:.2f} {to_unit}")
            break
        except InvalidInputError as e:
            print(e)
            print("Please try again.")

if __name__ == "__main__":
    main()


