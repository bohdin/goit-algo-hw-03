import re

def normalize_phone(phone_number):
    # Видаляємо все крім цифр та +
    pattern = r'[^0-9+]'
    replacement = ''
    normalize_phone_number = re.sub(pattern, replacement, phone_number)

    # Якщо номер поченається не з +38 
    if  not normalize_phone_number.startswith('+38'):
        # Перевіряємо два випадки
        if normalize_phone_number.startswith('38'): 
            # Коли є 38, додаємо +
            normalize_phone_number = '+' + normalize_phone_number 
        else: 
            # В інщому випадку додаємо +38
            normalize_phone_number = '+38' + normalize_phone_number 
    
    return normalize_phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)