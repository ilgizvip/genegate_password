import random

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += chars[random.randint(0, len(chars)-1)]
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

print('Введите количество паролей для генерации: ', end = '')
count_password = int(input())

print('Введите длину одного пароля: ', end = '')
len_password = int(input())

print('Включать ли цифры: ', end = '')
if input() == 'y':
    chars += digits

print('Включать ли прописные буквы: ', end = '')
if input() == 'y':
    chars += lowercase_letters

print('Включать ли строчные буквы: ', end = '')
if input() == 'y':
    chars += uppercase_letters

print('Включать ли символы (!#$%&*+-=?@^_?): ', end = '')
if input() == 'y':
    chars += punctuation

print('Исключать ли неоднозначные символы (il1Lo0O): ', end = '')
if input() == 'y':
    chars = ''.join([c for c in chars if not c in 'il1Lo0O'])

for i in range(count_password):
    print(generate_password(len_password, chars))