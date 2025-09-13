# Exercise: 4. Implementar método __str__ para todas as classes

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
        
    def __str__(self):
        return f'BankAccount(user={self.user}, password={self.password})'
        

class Person:
    def __init__(self, name: str, birthdate: str) -> None:
        """Initiate a Person object."""
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return f'Student(name={self.name}, birthdate={self.birthdate})'


class Student(Person):
    def __init__(self, name: str, birthdate: str, grade: str) -> None:
        super().__init__(name, birthdate)
        self.grade = grade

    def __str__(self):
        return f'Student(name={self.name}, birthdate={self.birthdate}, grade={self.grade})'


bank1 = BankAccount(user='rafael', password='1234')
person1 = Person(name='rafael', birthdate='1999-10-14')
student1 = Student(name='rafael', birthdate='1999-10-14', grade='A')
print(bank1)
print(person1)
print(student1)