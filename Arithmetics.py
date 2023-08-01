"""
This contains the four basic arithmetic operations
"""

class Arithmetics:
    def __init__(self, first_number: int, second_number: int) -> None:
        self.first_number = first_number
        self.second_number = second_number

    def addition(self) -> str:
        addition_result = self.first_number + self.second_number
        return f"{self.first_number} + {self.second_number} = {addition_result:,}"

    def subtraction(self) -> str:
        addition_result = self.first_number - self.second_number
        return f"{self.first_number} - {self.second_number} = {addition_result:,}"

    def division(self) -> str:
        if self.second_number == 0:
            return "Can't divide by 0"
        else:
            result = self.first_number / self.second_number
            return f"{self.first_number} ÷ {self.second_number} = {result:,}"

    def multiplication(self) -> str:
        result = self.first_number * self.second_number
        return f"{self.first_number} x {self.second_number} = {result:,}"