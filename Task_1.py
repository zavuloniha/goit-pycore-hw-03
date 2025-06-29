from datetime import datetime

current_date = datetime.today()
def get_days_from_today(date):
     formated_date = datetime.strptime(date, "%Y-%m-%d")
     difference = current_date - formated_date
     return difference.days
print(get_days_from_today('2025-9-07'))

