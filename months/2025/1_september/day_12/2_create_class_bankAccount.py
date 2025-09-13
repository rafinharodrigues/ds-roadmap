# Exercise: 2. Implementar classe BankAccount com deposit/withdraw/get_balance

class BankAccount:
    def __init__(self, user: str, password: str) -> None:
        """
        Initiate a bank account object.

        Args:
            user (str): Account username.
            password (str): Password for the account.
        """
        self._user = user
        self._password = password
        self._balance = 0.0

    @property
    def user(self):
        """Getter: Allow to access the self._user as an attribute."""
        return self._user 
    
    @property
    def password(self):
        """Getter: Allow to access the self._password as an attribute."""
        return self._password
    
    @property
    def balance(self):
        """Getter: Allow to access the self._balance as an attribute."""
        return self._balance
    
    def deposit(self, value: float) -> tuple[float, str]:
        """
        Add a value to the user bank account.

        Args:
            value (float): Value to deposit.

        Returns:
            tuple[float, str]:
                - value (float): The deposited value.
                - message (str): The deposit confirmation message.     
        """
        if value > 0:
            self._balance += value
            message = f'U${value} deposited.'
            return (value, message)
        else:
            raise ValueError('The deposited value should be > 0.')
        
    def withdraw(self, value: float) -> tuple[float, str]:
        """
        Subtracts a value from the bank account.

        Args:
            value (float): Value to withdraw.
        
        Returns:
            tuple[float, str]:
                - value (float): The value to withdraw.
                - message1 (str): The withdwaw confirmation message.
            message2 (str): The refused withdaw message if the withdraw
                            value is not valid.
        """
        if value <= self._balance:
            self._balance -= value
            message1 = f'U${value} withdrawn.'
            return (value, message1)
        else:
            message2 = 'Insufficient funds.'
            return message2


account1 = BankAccount(user='Rafael', password='password123')
print(account1.balance)

print(account1.deposit(-1))
print(account1.deposit(2))
print(account1.balance)
print(account1.withdraw(1.99))
print(account1.balance)