total = 0
while True:
    age = input()
    if age == "":
        break
    age = int(age)
    if 0 <= age <= 2:
        total += 0
    elif 3 <= age <= 12:
        total += 14
    elif age >= 65:
        total += 18
    elif 13 <= age <= 64:
        total += 23
print(f'Total cost is ${total:.2f}')
