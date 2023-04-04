path = 'file.txt'
phone_book = []


def menu():
    return int(input('''Главное меню:
    1. Открыть файл
    2. Показать все контикты
    3. Найти контакт
    4. Изменить контакт
    5. Добавить контакт
    6. Сохранить
    7. Удалить контакт
    8. Выход
    Выберете пункт меню:  '''))


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(',')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}
        phone_book.append(contact)


def show_data(book: list[dict], error: str):
    if not book:
        print(error)
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}, {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')


def search():
    with open(path, 'r', encoding='UTF-8') as file:
        book = file.read().split('\n')
        inp = input('Введите данные поиска: ')
    print('''
Найдено:
     ''')
    for i in book:
        if inp in i:
            print(i)


def add_contact() -> dict:
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    contact = {'name': name, 'phone': phone, 'comment': comment}
    phone_book.append(contact)
    return contact


def input_index(message: str):
    return int(input(message))


def change_contact1(contact: dict, index: int):
    phone_book.pop(index-1)
    phone_book. insert(index-1, contact)


def change_contact(book: list[dict], index: int):
    print('Введите новые данные или оствьте пустое поле, если нет изменений')
    contact = add_contact()
    phone_book.pop()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}


while True:
    choice = menu()
    match choice:
        case 1:
            print('''
****************************
       ФАЙЛ ОТКРЫТ
****************************
     ''')
            open_file()
        case 2:
            print('''
****************************
     СПИСОК КОНТАКТОВ
****************************
     ''')
            show_data(phone_book, "ERROR")

        case 3:
            print('''
****************************
    ПОИСК КОНТАКТА 
****************************
     ''')
            search()
            print('''
****************************
     ''')
        case 4:
            print('''
****************************
     СПИСОК КОНТАКТОВ
****************************
     ''')
            show_data(phone_book, "ERROR")
            index = input_index("введите номер изменяемого контакта: ")
            contact = change_contact(phone_book, index)
            change_contact1(contact, index)
        case 5:
            add_contact()
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
