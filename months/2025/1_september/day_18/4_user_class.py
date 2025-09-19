# Exercise: 4. Criar classe Database e classe User que usa Database

class Database:
    def __init__(self, name: str) -> None:
        """Initiate a Database object."""
        self.name = name


class User:
    def __init__(self, name: str) -> None:
        """Initiate a User object."""
        self.name = name
        self.database = Database(name='bahamas')