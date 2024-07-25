class Calculator:
    def __init__(self, number_a: int, number_b: int) -> None:
        self.number_a = number_a
        self.number_b = number_b

        self.result = 0

    def add(self) -> int:
        return self.number_a + self.number_b

    def substract(self) -> int:
        return self.number_a - self.number_b

    def multiply(self) -> int:
        return self.number_a + self.number_b

    def divide(self) -> float:
        if self.number_b <= 0:
            return 0
        return self.number_a / self.number_b

def main():
    cal = Calculator(number_a=5, number_b= 10)
    res = cal.add()
    print("Res =", res)

if __name__ == "__main__":
    main()
