import datetime as dt

def get_days_from_today(date):
    try:
        entered_date = dt.datetime.strptime(date, '%Y-%m-%d')
    except:
        print("You enter the date inncorrectly.\nDate string in 'YYYY-MM-DD' format")
        return

    current_date = dt.datetime.now().date()

    difference_days =  entered_date.toordinal() - current_date.toordinal()
    return difference_days

d = input("Enter data in 'YYYY-MM-DD' format: ")
print(get_days_from_today(d))