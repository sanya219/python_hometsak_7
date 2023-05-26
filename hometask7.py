# Задача 1
# Создайте пользовательский аналог метода map().

def user_map(func, i):
    result = []
    for item in i:
        result.append(func(item))
    return result

numbers = [1, 2, 3, 4, 5]
squared_numbers = user_map(lambda x: x ** 2, numbers)
print(squared_numbers)

# Задача 2
# Создайте декоратор, повторяющий функцию заданное количество раз.

def repeat_function(num_repeats):
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_function

@repeat_function(3)  # Повторить функцию 3 раза
def greet():
    print("Привет, мир!")

greet()

import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Глобальная переменная для хранения загаданного числа
secret_number = None
# Глобальная переменная для хранения количества попыток
attempts = 0

def start(update: Update, context: CallbackContext):
    global secret_number, attempts
    secret_number = random.randint(1, 1000)
    attempts = 0
    update.message.reply_text("Привет! Я загадал число от 1 до 1000. Попробуй угадать!")

def guess_number(update: Update, context: CallbackContext):
    global secret_number, attempts
    user_number = int(update.message.text)
    attempts += 1

    if user_number == secret_number:
        update.message.reply_text(f"Поздравляю, ты угадал число {secret_number} за {attempts} попыток!")
        secret_number = None
    elif user_number < secret_number:
        update.message.reply_text("Загаданное число больше.")
    else:
        update.message.reply_text("Загаданное число меньше.")

def main():
    updater = Updater("***********************")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, guess_number))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
