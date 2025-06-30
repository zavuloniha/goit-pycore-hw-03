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
        if current_year_birthday >= current_date and difference < 7 :
            new_user_data = {"name": user["name"], "congratulation_date": current_year_birthday.strftime("%Y.%m.%d")}
            next_birthdays.append(new_user_data)
        elif current_year_birthday >= current_date and difference < 7 and birthday_week_day == 6:
            new_congratulation_date = (current_year_birthday + timedelta(days=1)).strftime("%Y.%m.%d")
            new_user_data = {"name": user["name"], "congratulation_date": new_congratulation_date}
            next_birthdays.append(new_user_data)
        else:
            if current_year_birthday < current_date:
                new_congratulation_date = (current_year_birthday + timedelta(days=365)).strftime("%Y.%m.%d")
                new_user_data = {"name": user["name"], "congratulation_date": new_congratulation_date}
                next_birthdays.append(new_user_data)
             #не дуже було зрозумило з завдання що з цією перевіркою робити: 
             # "чи вже минув день народження в цьому році. Якщо так, розгляньте дату на наступний рік."
             # тому залишила дату наступного року при виведенні
           
    return next_birthdays   

print("Список привітань на цьому тижні:", get_ucoming_birthdays(users))   

