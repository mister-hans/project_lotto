
import random as rd

user_numbers = []

for i in range(6):
    user_numbers.append(int(input("Enter number (1-49): ")))

drawed_numbers = []

for i in range(49):
    drawed_numbers.append(i+1)
    
for i in range(43):
    drawed_numbers.remove(rd.choice(drawed_numbers))


compered_list = []
compered_list.extend(user_numbers)
compered_list.extend(drawed_numbers)


print("Drawed numbers is {}".format(drawed_numbers))
print("User choice is {}".format(user_numbers))
print("Compered list is {}".format(compered_list))
