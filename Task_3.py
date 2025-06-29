import re
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


def normalize_phone(phone_number):
    pattern = r"[\s\-\\)\(t\\n]"
    removing = ""
    formatted_phone = re.sub(pattern, removing, phone_number)
    
    for el in formatted_phone:
        if el[0] == "+":
           return formatted_phone
        elif el[0] == "0":
            formatted_phone1 = "+38" + formatted_phone
            return formatted_phone1  
        else: 
            formmatted_phone2 = "+" + formatted_phone
            return formmatted_phone2
         

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
