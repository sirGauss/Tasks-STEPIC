num1 = float(input())
num2 = float(input())
op = input()
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/' and num2 == 0:
    print('Деление на 0!')
elif op == '/' and num2 != 0:
    print(num1 / num2)
elif op == '*':
    print(num1 * num2)
elif op == 'mod' and num2 == 0:
    print('Деление на 0!')
elif op == 'mod' and num2 != 0:
    print(num1 % num2)
elif op == 'pow':
    print(num1 ** num2)
elif op == 'div' and num2 == 0:
    print('Деление на 0!')
elif op == 'div' and num2 != 0:
    print(num1 // num2)
