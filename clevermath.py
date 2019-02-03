number_a = int(input('Введите математическое число a:\n'))
operator = input('Введите математический оператор\n')
number_b = int(input('Введите число b:\n'))
if operator == ('+'):
    print(number_a + number_b)
elif operator == ('-'):
    print(number_a - number_b)
elif operator == ('*'):
    print(number_a * number_b)
elif operator == ('/'):
    print(number_a / number_b)
else:
    print('Указан неверный оператор')

print('Введите "exit", когда захотите выйти')

while True:
    word = input ('Хотите выйти?\n')
    if word == 'exit':
        break
    else:
        number_a = int(input('Введите математическое число a:\n'))
