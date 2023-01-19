# Генератор безопасных паролей

## Описание проекта

Программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить

## Составляющие проекта

* Целые числа (тип int);
* Переменные;
* Ввод / вывод данных (функции input() и print());
* Условный оператор (if/elif/else);
* Цикл for;
* Написание пользовательских функций;
* Работа с модулем random для генерации случайных чисел.

## Алгоритм

### Заголовок программы

* Подключите модуль random;
* Создайте строковые константы:
    * digits: 0123456789;
    * lowercase_letters: abcdefghijklmnopqrstuvwxyz;
    * uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
    * punctuation: !#$%&*+-=?@^_.
* Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.

### Считывание пользовательских данных

Программа должна запрашивать у пользователя следующую информацию:

* Количество паролей для генерации;
* Длину одного пароля;
* Включать ли цифры 0123456789?
* Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
* Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
* Включать ли символы !#$%&*+-=?@^_?
* Исключать ли неоднозначные символы il1Lo0O?

### Настройка генерируемых паролей

На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы, которые могут быть в генерируемом пароле.

### Генерации пароля

* Напишите функцию `generate_password()`, которая принимает два аргумента:

    * `length`: длину пароля;
    * `chars`: алфавит из символов которого состоит пароль;
* и возвращает пароль.
* используя цикл for, сгенерируйте необходимое количество паролей.
