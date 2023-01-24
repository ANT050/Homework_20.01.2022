def main_menu() -> int:  # +
    print('\n\033[33mГлавное меню:\033[0m\n')
    menu_list = ['Открыть справочник',
                 'Сохранить справочник',
                 'Показать все контакты',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт по id',
                 'Поиск контакта по id',
                 'Поиск контакта по параметрам',
                 'Выход']

    for i in range(len(menu_list) - 1):
        print(f'\t{i + 1}. {menu_list[i]}')
    print(f'\t{0}. {menu_list[-1]}')

    user_input = int(input('\n\033[33mВведи команду >: \033[0m'))
    print()
    # TODO: сделать валидацию

    return user_input

# Функция вывода всех контактов
def show_all(db: list):  # +
    for i in range(len(db)):
        user_id = i + 1
        print(f'\t{user_id}', end='. ')
        for v in db[i].values():
            print(f'{v}', end=' ')
        print()

# Функция добавления контакта
def create_contact():
    print('\033[32mСоздание нового контакта:\033[0m\n')
    print("--"*70)
    new_contact = dict()
    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    print("--"*70)
    return new_contact

# Функция изменения контакта
def change_contact(count: int) -> (int, dict):
    id = get_id(count)
    if id != -1:
        if input(f'Вы уверены что хотите изменить контакт {id}?\n1 - Да\n2 - Нет\n') == '1':

            print('\033[31mИзменение контакта:\033[0m')
            print("--"*70)
            contact = {}
            keys = ['lastname', 'firstname', 'phone', 'comment']

            for key in keys:
                if key == 'lastname':
                    if input(f'Изменить поле "Фамилия"?{id}?\n1 - Да\n2 - Нет\n') == '1':
                        contact['lastname'] = input('\tВведите фамилию >: ')
                if key == 'firstname':
                    if input(f'Изменить поле "Имя"?{id}?\n1 - Да\n2 - Нет\n') == '1':
                        contact['firstname'] = input('\tВведите имя >: ')
                if key == 'phone':
                    if input(f'Изменить поле "Телефон"?{id}?\n1 - Да\n2 - Нет\n') == '1':
                        contact['phone'] = input('\tВведите телефон >: ')
                if key == 'comment':
                    if input(f'Изменить поле "Комментарий"?{id}?\n1 - Да\n2 - Нет\n') == '1':
                        contact['comment'] = input('\tВведите комментарий >: ')
                print("--"*70)
            return id - 1, contact
    else:
        print('\nДействие отменено')
        return -1, {}

# Функция удаления контакат
def delete_contact(count: int) -> int:
    id = get_id(count)
    if id != -1:
        if input(f'Уверены что хотите удалить контакт № {id}?\n1 - Да\n2 - Нет\n') == '1':
            return id - 1
    print("--"*70)
    print('\033[31mДействие отменено\033[0m')
    print("--"*70)
    return -1

# Функция поиска контакта по id
def get_id(count):
    ans = int(input('\033[34m\nВведите номер записи (id) в справочнике: \033[0m'))
    print("--"*70)
    if 0 < int(ans) <= count:
        return ans
    print('\033[31m\nТакого контакта не существует\n\033[0m')
    print("--"*70)
    return -1
  
# Функция вывода сообщения о выполнении
def display_message(message: str):
    print("\033[34m[+]\033[0m", message)
    print("--"*70)

# Функция вывода сообщения об ошибке
def display_error(message: str):
    print("\033[31m[!]\033[0m", message)
    print("--"*70)

# Функция поиска контакта по параметрам
def search_by_parameters(db: list):
    print("Поиск по:")
    print("1. Фамилии")
    print("2. Имени")
    print("3. Фамилии и Имени")
    print("4. Номеру телефона")
    print("0. Отменить поиск")

    keys = ['lastname', 'firstname', 'phone', 'comment']
    record = {}

    while record == {}:
        search_by = int(input("\nВведите число, соответствующее параметру: "))

        if search_by == 1:
            record[keys[0]] = input("Введите фамилию для поиска: ")
            print("--"*70)
        elif search_by == 2:
            record[keys[1]] = input("Введите имя для поиска: ")

        elif search_by == 3:
            record[keys[0]] = input("Введите фамилию для поиска: ")
            record[keys[1]] = input("Введите имя для поиска: ")

        elif search_by == 4:
            record[keys[2]] = input("Введите номер телефона для поиска: ")
        
        elif search_by == 0:
          break

        else:
          print("Неверный ввод. Пожалуйста, введите число от 1 до 4.")
    return record

# Функция вывода контакта по id
def show_contact(id, rec):
    print(f'\t{id + 1}', end='. ')
    for v in rec.values():
        print(f'{v}', end=' ')
    print()

 # Функция выхода из программы
def exit_program():
    print('Завершение программы.')
    n = int(input('Вы уверены что хотите выйти?\n1. Да\n2. Нет \n'))
    if n == 1:
        return 1
    else:
        print('Попробуйте вызвать "Завершение программы" еще раз...')

# Функция вывода сообщения о выполнении
def display_message(message: str):
    print("\033[34m[+]\033[0m", message)
    print("--"*70)

# Функция вывода сообщения об ошибке
def display_error(message: str):
    print("\033[31m[!]\033[0m", message)
    print("--"*70)

