"""
This is used to find the value of a number raised to a certain power
"""

class Exponential:
    def __init__(self, operand: int, power: int) -> None:
        self.operand = operand
        self.power = power

    """Converts numbers from 0 -> 9 to superscripts"""
    def to_superscript(number: str) -> str:
        superscript_map = {
            '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
            '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
        }
        return superscript_map[number]

    def __str__(self) -> str:
        result = self.operand ** self.power
        result = f"{result:,}" if result < 10000000 else f"{result:.2e}"
        if len(str(self.power)) >= 2:
            lem = [Exponential.to_superscript(e) for e in str(self.power)]
            return f"{self.operand}{''.join(lem)} = {result}"
        else:
            power = Exponential.to_superscript(str(self.power))
            return f"{self.operand}{power} = {result}"