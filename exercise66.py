num = 0
total = 0
while True:
    letter = input()
    if letter == "":
        break
    elif letter == 'A+':
        num += 1
        total += 4.0
    elif letter == 'A':
        num += 1
        total += 4.0
    elif letter == 'A-':
        num += 1
        total += 3.7
    elif letter == 'B+':
        num += 1
        total += 3.3
    elif letter == 'B':
        num += 1
        total += 3.0
    elif letter == 'B-':
        num += 1
        total += 2.7
    elif letter == 'C+':
        num += 1
        total += 2.3
    elif letter == 'C':
        num += 1
        total += 2.0
    elif letter == 'C-':
        num += 1
        total += 1.7
    elif letter == 'D+':
        num += 1
        total += 1.3
    elif letter == 'D':
        num += 1
        total += 1.0
    elif letter == 'F':
        num += 1
        total += 0
average = total / num
print(average)



