import random

def get_numbers_ticket(min, max, quantity):
    # Перевіряємо вхідні параметри
    if min < 1 or max > 1000 or min > quantity > max:
        return [] # Повертаємо пустий список, якщо вхідні параметри неправильні
    else:
        # Створюємо пусту множину
        my_list = set()

        # Додаємо числа поки їх не буде потрібної кількості
        while(len(my_list) != quantity):
            my_list.add(random.randint(min, max))

        # З множини робимо список і сортуємо його
        my_list = list(my_list)
        my_list.sort()
        return my_list
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)