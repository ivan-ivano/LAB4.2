# < Іваньо Іван >
# Лабораторна робота № 4.2
# Табуляція функції, заданої формулою: функція однієї змінної.
# Варіант 0.6


import math

X_start = int(input("X_поч: "))
X_end = int(input("X_кін: "))
dX = int(input("dX: "))

print('---------------------------')
print('|   X   |   Y   |')
print('---------------------------')

x = X_start

while x <= X_end:
    A = 5 * math.exp(3 * x)
    if x <= -1:
        B = 3 + math.sin(abs(x))
    elif -1 < x <= 3:
        B = 2 * math.exp(x / 4 - 1)
    else:
        B = 7 - math.sqrt(2 * (x ** 3))

    y = A - B

    print('|   '+str(x)+'   |   '+str(round(y, 3))+'   |')
    x += dX

print('---------------------------')
