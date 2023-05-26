# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

def file_read(document: str):  #открытие файла
    with open(document, 'r') as file:
        contacts = [line.strip().split(',') for line in file]
    return contacts


def file_save(document: str, new_contacts: list):  #сохранение файла
    with open(document, 'w') as file:
        for i in range(len(new_contacts)):
            for j in range(len(new_contacts[i])):
                contact = str(new_contacts[i][j]).replace('[', '').replace(']', '').replace('\'', '')
                if j == len(new_contacts[i]) - 1:
                    file.write(contact)
                    continue
                file.write(contact + ',')
            file.writelines('\n')


def contacts_output(contacts: list):  #выводит все контакты
    for contact in range(len(contacts)):
        print(contacts[contact], end='\n')


def contact_added(new_doc: list):  #добавление контакта
    print("Введите контакт c помощью ',' в качестве разделителя")
    new_contact = input()
    new_doc.append(new_contact)


def contact_find(contacts: list, search_lists: list):  #поиск контакта
    contact_search = input("Какой контакт хотите найти? ")
    for i in range(len(contacts)):
        for j in range(len(contacts[i])):
            if str(contacts[i][j]) == contact_search:
                search_lists.append(contacts[i])
    return search_lists


def contact_change(contacts: list): #редактирование контакта
    change_contact = input("Какой контакт хотите изменить? ")
    for i in range(len(contacts)):
        for j in range(len(contacts[i])):
            if str(contacts[i][j]) == change_contact:
                change = input("Введите контакт с помощью разделителя \",\" ")
                contacts[i] = change.strip().split(',')


#  Удалить контакт
def contact_del(contacts: list):
    del_any = input("Кого вы хотите удалить? ")
    for i in range(len(contacts)):
        for j in range(len(contacts[i])):
            if contacts[i][j] == del_any:
                contcts = contacts.pop(i)
    return contacts
   


# Вызов меню и его пунктов
main_file = 'file.txt'
lists_contacts = file_read(main_file)
all_command = {'1' :  contacts_output, '2' : contact_added, '3' : contact_find, '4' : contact_change, '5' : contact_del, '6' : file_save}
print("Выберите пункт \n"
      "1 - показать все контакты\n"
      "2 - добавить контакт\n"
      "3 - найти контакт\n"
      "4 - редактировать контакт\n"
      "5 - удалить контакт\n"
      "6 - сохранение файла\n")
      
while True:
    command = input('Команда: > ')
    if command in all_command:
        all_command[command](main_file)
    else:
        print(' command error!')