#!/usr/bin/python3
import sys
import calculator_1 as calc


def calculate(num1, op, num2):
    result = 0
    if op == "+":
        result = calc.add(num1, num2)
    elif op == "-":
        result = calc.sub(num1, num2)
    elif op == "*":
        result = calc.mul(num1, num2)
    elif op == "/":
        result = calc.div(num1, num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return None
    return result


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    op = sys.argv[2]
    num2 = int(sys.argv[3])

    result = calculate(num1, op, num2)
    if result is None:
        sys.exit(1)

    print(f"{num1} {op} {num2} = {result}")
