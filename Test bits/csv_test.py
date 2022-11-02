import csv

a = [234234234, 345345, 345345345]
with open('test.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(a)


with open('test.csv') as file:
    main_list = file.read().split(',')


print(main_list)