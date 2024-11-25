my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index < len(my_list):
    qbit = my_list[index]
    if qbit < 0:
        break
    if qbit == 0:
        index += 1
        continue

    print(qbit)

    index += 1
