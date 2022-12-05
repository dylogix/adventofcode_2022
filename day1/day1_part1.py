with open("day1/data.txt", "r") as data_file:
    values = data_file.readlines()

result = 0
counter = 0
tmp = 0

for value in values:
    if value != '\n':
        tmp += int(value)
    else:
        if tmp > result:
            result = tmp
        tmp = 0
        counter += 1

print(result)