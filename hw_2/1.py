import csv
import locale
import re

file_coding = locale.getpreferredencoding()


def get_data():
    files_name = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"], [], [], []]
    os_prod_list = []
    os_name_list = []
    os_code_list =[]
    os_type_list = []

    for file in files_name:
        with open('files/' + file, encoding=file_coding) as f:
            data = f.readlines()
            for res in data:
                if re.search("Изготовитель системы", res):
                    os_prod_list.append(res.split(':')[-1].strip())
                if re.search("Название ОС", res):
                    os_name_list.append(res.split(':')[-1].strip())
                if re.search("Код продукта", res):
                    os_code_list.append(res.split(':')[-1].strip())
                if re.search("Тип системы", res):
                    os_type_list.append(res.split(':')[-1].strip())

    i = 0
    k = 1
    while k <= len(files_name):
        main_data[k].append(os_prod_list[i])
        main_data[k].append(os_name_list[i])
        main_data[k].append(os_code_list[i])
        main_data[k].append(os_type_list[i])
        i += 1
        k += 1

    return main_data


def write_to_csv(file_csv):
    data = get_data()

    with open(file_csv, 'w', encoding=file_coding) as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


write_to_csv('files/result.csv')
