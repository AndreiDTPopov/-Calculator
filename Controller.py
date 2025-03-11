from model import addition, subtraction, multiplication, division
from view import numbers, roperation, equals

def run():
    a, b = numbers()
    operation = roperation()

    if operation == '+':
        equally = addition(a, b)
    elif operation == '-':
        equally = subtraction(a, b)
    elif operation == '*':
        equally = multiplication(a, b)
    elif operation == '/':
        equally = division(a, b)
    else:
        equally = "Перестаньте играть шлакоблоком в хэдис!!!"

    equally(result)

if __name__ == "__main__":
    run()