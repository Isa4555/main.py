from colorama import init
from colorama import Style, Fore, Back
init()

print(Fore.CYAN)
print(Back.LIGHTBLACK_EX)
gay = input(" Cен гейсынба? : ")
if gay == "Нет":
    print("Отирик айтпа")
elif gay == "Да":
    print("Былдымо")
else:
    print("Нормально жауап берсей")

input()