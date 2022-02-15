my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(*my_list,)

my_list.insert(1, '"')
my_list.insert(3, '"')
my_list.insert(5, '"')
my_list.insert(7, '"')
my_list.insert(12, '"')
my_list.insert(14, '"')

print(my_list)

input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for _ in range(len(input_list)):

    elem = input_list.pop(0)

    if elem.isdigit() and elem.isalnum():
        input_list.append(f'"{int(elem):02d}"')
        # or   ['"', "00", '"']
        # input_list.append('"')
        # input_list.append(f'{int(elem):02d}')
        # input_list.append('"')


    elif elem[0] == "+" and elem[1].isdigit():
        input_list.append(f'"+{int(elem):02d}"')
        # or   ['"', "+00", '"']
        # input_list.append('"')
        # input_list.append(f'+{int(elem):02d}')
        # input_list.append('"')

    else:
        input_list.append(elem)


print(' '.join(input_list))