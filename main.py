"""
This is a calculator app
"""

from Exponential import Exponential
from Arithmetics import Arithmetics


if __name__ == "__main__":
    print("\nUse: \n'+' for addition; \n'-' for subtraction; \n'x' or '*' for multiplication; \n'/' or '÷' for division; \n'**' or '^' for power and; \n'√' or 'r' for root operations\n\n<------------------------------------->\n")
    print("Example: \n2 + 4")


    try:
        while True:

            equation = input("\nEnter operation below(enter 'stop' to end):\n")
            if equation == 'stop':
                break
            else:
                equation = equation.split()
                firstNumber = int(equation[0])
                operator = equation[1]
                secondNumber = int(equation[2])

                match operator:
                    case "+":
                        calculate = Arithmetics(firstNumber, secondNumber).addition()
                        print(calculate)
                        
                    case "-":
                        calculate = Arithmetics(firstNumber, secondNumber).subtraction()
                        print(calculate)
                    
                    # multiplication
                    case "x":
                        calculate = Arithmetics(firstNumber, secondNumber).multiplication()
                        print(calculate)
                    case "*":
                        calculate = Arithmetics(firstNumber, secondNumber).multiplication()
                        print(calculate)
                    
                    # division
                    case "/":
                        calculate = Arithmetics(firstNumber, secondNumber).division()
                        print(calculate)
                    case "÷":
                        calculate = Arithmetics(firstNumber, secondNumber).division()
                        print(calculate)
                    
                    # exponent
                    case "**":
                        calculate = Exponential(firstNumber, secondNumber)
                        print(calculate)
                    case "^":
                        calculate = Exponential(firstNumber, secondNumber)
                        print(calculate)
                    
                    # root
                    case "√":
                        calculate = Arithmetics(firstNumber)
                        print(calculate)
                    case "r":
                        calculate = Arithmetics(firstNumber)
                        print(calculate)
                        
                    case _:
                        print('Invalid operation')

    except Exception as error:
            print(f"There's something wrong somewhere \n{error}")