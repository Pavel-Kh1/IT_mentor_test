def main(input_str:str):
    try:
        parts = input_str.split()

        if len(parts) > 3:
            raise ValueError("Формат выражения не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
        if len(parts) < 3:
            raise ValueError("Строка не является математической операцией")

        a, operation, b = parts

        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise ValueError("Калькулятор работает только с целыми числами")

        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно.")

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            result = a // b  # Целочисленное деление
        else:
            raise ValueError("Неподдерживаемая операция. Допустимые операции: +, -, *, /.")

        return str(result)

    except ValueError as e:
        return str(e)

while True:
    input_str = input("Введите выражение (например, '5 + 3'): ")
    result = main(input_str)
    print("Результат:", result)