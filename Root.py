from sympy import sqrt, simplify


class Root:
    def __init__(self, first_number: int = None, second_number: int = None) -> None:
        self.first_number = first_number
        self.second_number = second_number

    # TODO: refactor this to find the square root of perfect squares and return non perfect squares in surd form

    def __str__(self) -> str:
        if self.second_number is None:
            square_root = sqrt(self.first_number)
            return f"√{self.first_number} = {square_root}"

        else:
            operation = self.first_number * sqrt(self.second_number)
            simp_toString = str(simplify(operation))
            remLast = simp_toString.replace(')', '')
            justNum = remLast.split('*sqrt(')
            return f"{justNum[0]}√{justNum[1]}"


root = Root(4, 1)
