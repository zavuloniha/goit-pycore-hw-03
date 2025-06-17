from datetime import datetime

current_date = datetime.today()
f_current_date = current_date.date()
def get_days_from_today(date):
    formated_date = datetime.strptime(date, "%Y-%m-%d")
    date_for_counting = formated_date.date()
    #difference = current_date - formated_date
    difference = f_current_date - date_for_counting
    #results = difference.date()
    #return results
    return difference
print(get_days_from_today('2036-5-25'))
