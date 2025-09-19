# Exercise: 5. Implementar User.save() que usa self.db.insert()

class Database:
    def __init__(self, name: str) -> None:
        """Initiate a Database object."""
        self.name = name

    def insert(self, user: str) -> None:
        """Insert a user into database."""
        print(f'User "{user}" inserted.')


class User:
    def __init__(self, username: str) -> None:
        """Initiate a User object."""
        self.username = username
        self.db = Database(name='bahamas')

    def save(self) -> None:
        """Save's a user to the database."""
        self.db.insert(self.name)