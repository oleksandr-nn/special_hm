## Анкета для відправлення посилки
# Дані про відправника
your_name = input("Please enter your name: ")
your_surname = input("Please enter your surname: ")
your_father_name = input("Please enter your father's name: ")
your_phone = int(input("Please enter your phone number: "))
adress_to_go=input("Please enter post adress: ")

# Дані про отримувача
recipients_name = input("Please enter your recipient's name: ")
recipients_surname = input("Please enter your recipient's surname: ")
recipients_father_name = input("Please enter your recipient's father's name: ")
recipients_phone_number = int(input("Please enter your recipient's phone number: "))

# Дані про посилку:
mass=int(input("Please enter mass: "))
value=int(input("Please enter value: "))

print(your_name + your_surname, your_father_name,", that has phone number", your_phone,",", "send package to", recipients_name,
recipients_surname, recipients_father_name,", that has phone number", recipients_phone_number, "to", adress_to_go, "adress",
".", "Package has", mass, "mass and", value, "value")

print(f"{your_name} {your_surname} {your_father_name}, that has phone number {your_phone}, send package to {recipients_name}"
      f"{recipients_surname} {recipients_father_name}, that has phone number {recipients_phone_number}, to {adress_to_go}"
      f". Package has {mass} mass and {value} value")
