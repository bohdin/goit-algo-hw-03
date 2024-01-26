from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Конвертуємо рядки в об'єкти datetime.date
    for user in users:
        user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

    # Отримуємо поточну дату
    today = datetime.today().date()

    # Створюємо порожній список для зберігання інформації про майбутні дні народження
    upcoming_birthdays = []

    for user in users:
        # Створюємо словник для зберігання інформації про майбутні дні народження
        upcoming_birthday = dict()

        # Змінює рік на поточний
        birthday_this_year = user['birthday'].replace(year = today.year)
        
        # Перевіряємо, чи минув день народження в цьому році
        if birthday_this_year < today:
            # Якщо так, розглядаємо дату наступного року
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        
        # Визначаємо різницю в днях між сьогоднішньою датою і датою народження
        difference = birthday_this_year.toordinal() - today.toordinal()
        if difference < 7: # Перевіряємо чи день народження буде протягом наступних 7 днів
            # Переносимо день народження, якщо випадає на вихідні
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            if birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            # Зберігаємо дату у словник
            upcoming_birthday['name'] = user['name']
            upcoming_birthday['birthday'] = birthday_this_year.strftime('%Y.%m.%d')
            # Додаємо словник до списку
            upcoming_birthdays.append(upcoming_birthday)
        
    return upcoming_birthdays
        
            
            
            
            

users = [
    {"name": "John Doe", "birthday": "1985.01.26"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1995.05.10"},
    {"name": "Bob Anderson", "birthday": "1988.11.03"},
    {"name": "Eva Miller", "birthday": "1992.09.15"},
    {"name": "Charlie Brown", "birthday": "1980.03.21"},
    {"name": "Grace Taylor", "birthday": "1998.08.05"},
    {"name": "Daniel Clark", "birthday": "1993.12.12"},
    {"name": "Sophie Turner", "birthday": "1987.01.28"},
    {"name": "Michael Jordan", "birthday": "1963.01.30"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)