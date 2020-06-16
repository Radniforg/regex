import re
from pprint import pprint
import csv

def LFS(list_name):
    new_list = []
    if re.search(' ', list_name[0]):
        new_list = re.split(' ', list_name[0])
    else:
        new_list.append(list_name[0])
        if re.search(' ', list_name[1]):
            first_sur_list = re.split(' ', list_name[1])
            for name in first_sur_list:
                new_list.append(name)
        else:
            new_list.append(list_name[1])
            new_list.append(list_name[2])
    return new_list


def phone(number):
    space_deletion = re.sub(' ', '', number)
    additional_number = re.sub('д', ' д', space_deletion)
    plus_check = re.match('\+7', additional_number)
    if not plus_check:
        plus = re.sub('^8', '+7', additional_number)
    else:
        plus = additional_number
    bracket_check = re.search('\(', plus)
    if not bracket_check:
        brackets = re.sub('(\+7)(...)', r'\1(\2)', plus)
    else:
        brackets = plus
    tile_check = re.search('-', brackets)
    if not tile_check:
        tiles = re.sub('(\+7........)(..)', r'\1-\2-', brackets)
    else:
        tiles = brackets
    add_bracket_check = re.search('\( д', tiles)
    if add_bracket_check:
        formated_phone = re.sub('(\()( ........)(\))', r'\2', tiles)
    else:
        formated_phone = tiles
    return formated_phone

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)


#[5] - телефон

for contacts in contacts_list[1:]:
    new_name_list = LFS(contacts[:3])
    contacts[:3] = new_name_list[:3]
    contacts[5] = phone(contacts[5])

pprint(contacts_list)