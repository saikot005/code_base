class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calc(self):
        if self.num1 != 0 and self.num2 != 0:
            return (
                f'Add: {self.num1 + self.num2}\n'
                f'Sub: {self.num1 - self.num2}\n'
                f'Mult: {self.num1 * self.num2}\n'
                f'Div: {self.num1 / self.num2}\n'
                f'Cube: {self.num1 ** 3}, {self.num2 ** 3}\n'
                f'Square: {self.num1 ** 2}, {self.num2 ** 2}\n'
            )
        else:
            return 'Please provide valid input numbers'


def main():
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    cal_obj = calculator(num1, num2)
    result = cal_obj.calc()
    print(result)


if __name__ == "__main__":
    main()
