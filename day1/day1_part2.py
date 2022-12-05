with open("day1/data.txt", "r") as data_file:
    values = data_file.readlines()

result = []
counter = 0
tmp = 0

for value in values:
    if value != '\n':
        tmp += int(value)
    else:
        result.append(tmp)
        tmp = 0
        counter += 1

result.sort(reverse=True)
result = result[0] + result[1] + result[2]

print(result)