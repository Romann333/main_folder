import csv

a = ['name', 'tel', 'id']
with open('test.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        a
    )

b =[1, '1, 2, 5, 5, 4, 4,f ,f ,f ,\nfkjfkdjfsosdkjfoisjdofijsodifjsskdjfodjsfosdjf', 2, 4, 4, ] 
with open('test.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(
        b
    )