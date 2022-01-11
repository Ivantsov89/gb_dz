def sum_list_1(dataset: list):
    result = 0
    for value in dataset:
        sum_nums = 0
        i = value
        while i > 0:
            digital = i % 10
            sum_nums += digital
            i = i // 10
        if sum_nums % 7 == 0:
            result += value
    return result

my_list = [i**3 for i in range(1, 1001, 2)]
my_list_2 = [(i**3 + 17) for i in range(1, 1001, 2)]

result_1 = sum_list_1(my_list)
print(result_1)

result_2= sum_list_1(my_list_2)
print(result_2)