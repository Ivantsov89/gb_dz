from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    for i in range(len(list_in)):
        str_el = "{:2.2f}".format(list_in[i])
        ind = str_el.find('.')
        list_in[i] = f'{str_el[:ind]:} руб. {str_el[ind + 1:]} коп.'
    str_out =','.join(list_in)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in

print(id(my_list))
result_2 = sort_prices(my_list)
print(result_2)
print(id(result_2))

def sort_price_adv(list_in: list) -> list:
    list_out = list(reversed(list_in))
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    list_in = list(reversed(list_in))
    list_out = list_in[0:5]

    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)