my_list = [x**3 for x in range (1,1000,2)]
def sum_digits(num):
    res = 0
    while num != 0:
        res += num % 10
        num //= 10
    return res

def sum_list_1(dataset: list) -> int:
    sum1 = 0
    list1 = []
    for elem in dataset:
        a = sum_digits(elem)

        if a % 7 == 0:
            list1.append(elem)

    for x in list1:
        sum1 += x
    return sum1

def sum_list_2(dataset: list) -> int:
    sum2 = 0
    list2 = []
    for elem in dataset:
        b = elem + 17
        a = sum_digits(b)
        if a % 7 == 0:
            list2.append(b)
    for elem in list2:
        sum2 += elem
    return sum2

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
