type_of_room = input()
if type_of_room == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c))**0.5)
elif type_of_room == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif type_of_room == 'круг':
    r = float(input())
    pi = 3.14
    print(pi * r**2)
