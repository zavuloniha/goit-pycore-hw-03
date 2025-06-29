from datetime import datetime, date, timedelta

users = [
    {"name": "Jack Vong", "birthday": "1985.06.30"},
    {"name": "John Doe", "birthday": "1981.04.02"},
    {"name": "Jane Smith", "birthday": "1990.07.03"},
    {"name": "Tom Ford", "birthday": "1980.06.29"},
    {"name": "Lucie Lee", "birthday": "1991.07.06"},
    {"name": "Anny Tod", "birthday": "1999.08.25"}
]
next_birthdays = []
current_date = datetime.today().date() 

def get_ucoming_birthdays(users):
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        current_year_birthday = date(current_date.year,  user_birthday.month, user_birthday.day)
        difference = (current_year_birthday - current_date).days
        birthday_week_day = current_year_birthday.weekday()
        if current_year_birthday < current_date:
           new_congratulation_date1 = current_year_birthday + timedelta(days=365)
           new_congratulation_date1_formatted = new_congratulation_date1.strftime("%Y.%m.%d")
           new_user_data1 = {"name": user["name"], "congratulation_date": new_congratulation_date1_formatted}
           next_birthdays.append(new_user_data1)
           #не дуже було зрозумило з завдання що з цією перевіркою робити: 
           # "чи вже минув день народження в цьому році. Якщо так, розгляньте дату на наступний рік."
           # тому залишила дату наступного року при виведенні
        elif difference <= 7 and user_birthday.month >= current_date.month:
            current_year_birthday_formatted = current_year_birthday.strftime("%Y.%m.%d")
            new_user_data2 = {"name": user["name"], "congratulation_date": current_year_birthday_formatted}
            next_birthdays.append(new_user_data2)
            if birthday_week_day == 6:
                new_congratulation_date2 = current_year_birthday + timedelta(days=1)
                new_congratulation_date2_formatted = new_congratulation_date2.strftime("%Y.%m.%d")
                new_user_data3 = {"name": user["name"], "congratulation_date": new_congratulation_date2_formatted}
                next_birthdays.append(new_user_data3)
       
           
    return next_birthdays   

print("Список привітань на цьому тижні:", get_ucoming_birthdays(users))   

