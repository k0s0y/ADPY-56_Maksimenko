import re
import csv
from pprint import pprint


# структура 'lastname,firstname,surname,organization,position,phone,email'
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер,
# формат будет такой: +7(999)999-99-99 доб.9999;
# объединить все дублирующиеся записи о человеке в одну.
# читаем адресную книгу в формате CSV в список contacts_list

def read_csv(data_file_name):
    with open(data_file_name, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


# TODO 1: выполните пункты 1-3 ДЗ
def format_fullname(contact_list):
    name_pattern = r'^([А-ЯЁа-яё]+)\s*(\,?)([А-ЯЁа-яё]+)\s*(\,?)([А-ЯЁа-яё]*)\s*(\,)?(\,?)(\,?)'
    name_repl = r'\1\2\8\3\4\7\5\6'
    contacts_list_replaced = list()
    for contact in contact_list:
        contact_string = ','.join(contact)
        contact_replaced = re.sub(name_pattern, name_repl, contact_string)
        contact_list = contact_replaced.split(',')
        contacts_list_replaced.append(contact_list)
    return contacts_list_replaced


def format_phone(contact_list):
    name_pattern = r'(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2}\s*)\(*(доб*\.)*\s*(\d+)*\)*'
    name_repl = r'+7(\2)\3-\4-\5\6\7'
    contacts_list_replaced = list()
    for contact in contact_list:
        contact_string = ','.join(contact)
        contact_replaced = re.sub(name_pattern, name_repl, contact_string)
        contact_list = contact_replaced.split(',')
        contacts_list_replaced.append(contact_list)
    return contacts_list_replaced


def remove_duplicate(contact_list):
    contacts_list_replaced = list()
    for i in contact_list:
        for j in contact_list:
            if (i[0] == j[0] and i[1] == j[1]) and i != j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
                if len(i) == 8:
                    i.pop()
        if i not in contacts_list_replaced:
            contacts_list_replaced.append(i)
    return contacts_list_replaced


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def write_file(contacts_list):
    with open("phonebook.csv", "w", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


contacts_list = read_csv('homework1_data.csv')
contacts_list = format_fullname(contacts_list)
contacts_list = format_phone(contacts_list)
contacts_list = remove_duplicate(contacts_list)
write_file(contacts_list)
# print(contacts_list)
