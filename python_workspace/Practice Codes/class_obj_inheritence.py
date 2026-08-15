"""Small examples of classes, objects, and inheritance in Python.

Run this file directly to see each example.
"""


class Person:
    """Represent an employee and determine a designation from their age."""

    # Each tuple contains the minimum age required for a designation.
    # The order is highest to lowest so the first matching value is correct.
    DESIGNATIONS = (
        (32, "SM"),  # Senior Manager
        (27, "M"),   # Manager
        (23, "SA"),  # Senior Associate
        (20, "A"),   # Associate
        (18, "PAT"), # Programmer Analyst Trainee
    )

    def __init__(self, name, company, age):
        """Create a Person object with basic employee information."""
        self.name = name
        self.company = company
        self.age = age

    def get_designation(self):
        """Return the designation that corresponds to this person's age."""
        for minimum_age, designation in self.DESIGNATIONS:
            if self.age >= minimum_age:
                return designation
        return "Not eligible"  # Handles ages below 18 clearly.

    def greet(self):
        """Return a readable summary of the object."""
        return f"{self.name} -> {self.company} -> {self.get_designation()}"


# Inheritance: User gets all attributes and methods from Person.
class User(Person):
    """A Person with an additional username."""

    def __init__(self, name, company, age, username):
        # super() calls the parent class constructor instead of duplicating it.
        super().__init__(name, company, age)
        self.username = username

    def greet(self):
        # Method overriding: extend the parent method with User-specific data.
        return f"{super().greet()} -> username: {self.username}"


class Manager(Person):
    """Another child class that adds the team a manager leads."""

    def __init__(self, name, company, age, team):
        super().__init__(name, company, age)
        self.team = team

    def introduce_team(self):
        return f"{self.name} leads the {self.team} team."


def main():
    """Create objects and demonstrate parent and child class behavior."""
    # Objects created from the parent class.
    john = Person("John", "Razor", 35)
    bob = Person("Bob", "Google", 18)
    intern = Person("Mia", "Razor", 17)

    print(john.greet())
    print(bob.greet())
    print(intern.greet())

    # A User can use Person.greet() because User inherits from Person.
    robi = User("Robi", "CT", 25, "robi25")
    print(robi.greet())

    # A different child class can add its own data and methods.
    alice = Manager("Alice", "Razor", 30, "Data Engineering")
    print(alice.greet())
    print(alice.introduce_team())

    # isinstance confirms that a child object is also an instance of its parent.
    print(f"Is Robi a Person? {isinstance(robi, Person)}")


# This prevents the examples from running when this file is imported elsewhere.
if __name__ == "__main__":
    main()
