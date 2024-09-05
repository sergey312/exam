class Employee:
    def __init__(self, full_name, role, telefon_number, email) -> None:
        self.full_name = full_name
        self.role = role
        self.telefon_number = telefon_number
        self.email = email

    def __repr__(self) -> str:
        return f"{self.full_name}, {self.role}, {self.telefon_number}, {self.email}"
