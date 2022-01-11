def convert_name_extract(list_in: list) -> list:
    return ["Привет, {}!".format(name.split()[-1].title()) for name in list_in]


input_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

print(convert_name_extract(input_names))