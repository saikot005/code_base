from datetime import datetime


class AgeCalculator:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    def calculate_age(self, current_year=None):
        if current_year is None:
            current_year = datetime.now().year
        return current_year - self.birth_year


def main():
    birth_year = int(input("Enter your dob year: "))
    age_calculator = AgeCalculator(birth_year)
    age = age_calculator.calculate_age()
    print(f"You are {age} years old.")


if __name__ == "__main__":
    main()
