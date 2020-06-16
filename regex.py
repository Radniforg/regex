import re
from pprint import pprint
import csv

def LFS(list_name):
    new_list = []
    if re.search(' ', list_name[0]):
        new_list = re.split(' ', list_name[0])
        if len(new_list) == 2:
            new_list.append('')
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

def duplicate_deletion(contact_list):
    marked = []
    for contacts in range(1, len(contact_list)):
        approach = 1
        while contacts + approach < len(contact_list):
            if contact_list[contacts][0] == contact_list[contacts + approach][0]:
                if contact_list[contacts][1] == contact_list[contacts + approach][1]:
                    marked.append(contacts + approach)
                    for detail in range(2, len(contact_list[contacts])):
                        if contact_list[contacts][detail] == '' or  contact_list[contacts][detail] == ' ':
                            contact_list[contacts][detail] = contact_list[contacts + approach][detail]
            approach += 1
    marked.sort(reverse=True)
    for duplicate in marked:
        del (contact_list[duplicate])
    return contact_list

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
pprint(contacts_list)

for contacts in contacts_list[1:]:
    new_name_list = LFS(contacts[:3])
    contacts[:3] = new_name_list[:3]
    contacts[5] = phone(contacts[5])

clean_list = duplicate_deletion(contacts_list)

with open("phonebook.csv", "w", newline = '') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(clean_list)