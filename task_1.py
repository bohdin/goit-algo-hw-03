from datetime import datetime as dt

def get_days_from_today(date):
    # Перетворюємо рядом у об'єкт datetime, якщо формат не вірний повертаємо None
    try:
        entered_date = dt.strptime(date, '%Y-%m-%d')
    except:
        print("You enter the date inncorrectly.\nDate string in 'YYYY-MM-DD' format")
        return

    # Отримуємо поточну дату
    current_date = dt.now().date()

    # Рахуємо різницю в днях між введеною датою та поточною
    difference_days =  entered_date.toordinal() - current_date.toordinal()
    return difference_days

d = input("Enter data in 'YYYY-MM-DD' format: ")
print(get_days_from_today(d))