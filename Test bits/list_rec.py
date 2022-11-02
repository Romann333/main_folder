a = [45545, 34342342, 342353464, 3545345345, ]

with open('trash_bin/list.txt', 'w') as file:
    print(*a, sep=',', file=file)



with open('trash_bin/list.txt') as f:
    main_list = [i.strip('\n') for i in f.read().split(',')]


print(main_list)