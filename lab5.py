#Задание 1 map filter
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 35, 65, 99, 120]
print(list(filter(lambda elem: elem < 5, list1)))
print(list(map(lambda x: x/2, list1)))
print(list(map(lambda x: x/2, filter(lambda x: x > 17, list1))))
print(sum(list(map(lambda x: x**2, filter(lambda x: 9 < x < 100 and x%9 == 0, list1)))))
#Задание 2 generator
from math import factorial
def factorials(n):
    x = [factorial(i) for i in range(1, n+1)]
    yield x
print(*list(factorials(7)))
#Задание 3
def fibonacci(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
        yield f1**2
print(*fibonacci(7))
#Задание 4
def generator():
    for i in range(ord('а'), ord('я')+1):
        yield chr(i)
print(*generator())
#Задание 5
for i in range(ord('а'), ord('я')+1):
    print(chr(i), end=' ')
#Задание 6 function as object
def arithmetic_operation(operation):
    if operation == '+':
        return lambda x,y: x+y
    elif operation == '-':
        return lambda x,y: x-y
    elif operation == '*':
        return lambda x,y: x*y
    elif operation == '/':
        return lambda x,y: x/y
operation = arithmetic_operation('+')
print(operation(1, 4))
#Задание 7
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1 if objects else True
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
#Задание 8
def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print(f'{operation(i, j):<4}', end=' ')
            print()
print_operation_table(lambda x, y: x*y, 5)
#Задание 9
def ask_password(login: str, password: str, success: callable, failure: callable):
    count_v, count_c, pos_c = 0, 0, 0
    for pos, symbol in enumerate(password.lower()):
        if symbol in "aeiouy":
            count_v += 1
        elif symbol in login.lower():
            count_c, pos_c = 0 if pos_c > pos else count_c + 1, pos
    if count_v < 3 and count_c < 3:
        failure(login, "Everything is wrong")
    elif count_v < 3:
        failure(login, "Wrong number of vowels")
    elif count_c < 3:
        failure(login, "Wrong consonants")
    else:
        success(login)
ask_password("login", "1",
    lambda login: print(f"SUCCES: #{login}"),
    lambda login, message: print(f"FAILURE: #{login} | info: {message}"))
#Задание 10 standard features
print(*sorted(input().split(), key=str.lower))
#Задание 11
list2 = [3, 6, -8, 2, -78, 1, 23, -45, 9]
list2.sort()
print(list2)
#Задание 12
my_list = [[4, 5], [0, 2], [1, 2], [1, 1], [5, 5], [7, 0], [0, 2], [1, 5], [0, 0]]
print(sorted(my_list, key=lambda x: (x[1] ** 2 + x[0] ** 2) ** 1 / 2))
#Задание 13
import sys
t = '''\
    64 33 79 56 78 70 45 71 82 3
    96 27 8 36 72 14 91 10 21 65
    95 28 91 23 78 38 21 50 64 37
    97 54 94 6 48 17 37 19 78 58
    69 58 35 1 70 24 60 17 3 11
    48 9 13 23 82 49 79 55 29 53
    9 2 67 90 0 17 34 55 49 63
    98 98 23 71 66 57 15 94 34 81
    58 37 32 29 10 19 53 46 95 19
    41 24 95 47 58 17 74 69 62 4 '''
print("0" in sys.stdin.read().split())
#Задание 14
with open('text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
lines = list(map(str.strip, lines))
for i, line in enumerate(lines):
    if line[-1] == ":":
        start = i
    elif line[-1] == '.':
        end = i
        break
print(lines[start+1: end+1])
#Задание 15
import sys
from functools import reduce

def find_min_lex(iterator):
    return reduce(lambda x, y: x if x < y else y, iterator)

lines = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    lines.append(line)

if lines:
    print(find_min_lex(lines))
else:
    print("")
#Задание 16
import sys
from functools import reduce
from math import gcd

def compute_gcd(numbers):
    return reduce(lambda x, y: gcd(x, y), numbers)

numbers = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    try:
        num = int(line)
        if num <= 0:
            print("Ошибка: все числа должны быть натуральными (положительными)", file=sys.stderr)
            sys.exit(1)
        numbers.append(num)
    except ValueError:
        print(f"Ошибка: '{line}' не является натуральным числом", file=sys.stderr)
        sys.exit(1)

if numbers:
    print(compute_gcd(numbers))
else:
    print("Ошибка: не введено ни одного числа", file=sys.stderr)
    sys.exit(1)
#Задание 17
def check_password(foo):
    def check():
        password = input()
        if password != '123':
            print('В доступе отказано')
            return None
        foo()
    return check()
@check_password
def hi():
    print('Hi')
#Задание 18
def check_password(correct_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            input_password = input("Введите пароль: ")
            if input_password == correct_password:
                return func(*args, **kwargs)
            else:
                raise PermissionError("Неверный пароль! Доступ запрещён.")
        return wrapper
    return decorator

# Пример использования
@check_password('secret123')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print(f"Готовим бургер с мясом {typeOfMeat}")
    if withOnion:
        print("Добавляем лук")
    if withTomato:
        print("Добавляем помидор")
    return "Бургер готов!"

# Тестирование
try:
    print(make_burger("говядина", withOnion=True))
except PermissionError as e:
    print(e)
#Задание 19
def cached(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Возвращаем кэшированный результат({args[0]})")
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"Вычисляем и кэшируем({args[0]}) = {result}")
        return result

    return wrapper

@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(5))
print(fib(5))