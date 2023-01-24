import model
import view


# Функция чтения справочника из файла
def open_reference( file_name: str = "test.txt" ) -> list:
    reference, status = model.read_reference_from_file( file_name )
    if status:
        view.display_message(f"\033[34mЧтение справочника из файла {file_name} выполнено успешно \033[0m\n")
    else:
        view.display_error(f"\n\033[34mОшибка чтения справочника из файла: {file_name}\033[34m\n")
    return reference

# Функция записи справочника в файл
def save_reference( file_name: str = "test.txt", reference: list = model.reference ) -> None:
    status = model.write_reference_from_file( file_name, reference )
    if status:
        view.display_message(f"\033[34mСправочник {file_name} успешно сохранен\033[0m\n")
    else:
        view.display_error(f"\n\033[34mОшибка сохранения справочника: {file_name}\033[34m\n")

# Функция просмотра всех контактов
def show_contacts( count: int = 0 ) -> list:
    reference, status = model.get_reference(count)
    if not status:
        view.display_error("Внимание: Количество записей в справочнике меньше запрошенного")
    return reference

# Функция добавления нового контакта
def add_contact(record: dict) -> list:
    reference, status = model.add_reference(record)
    if status:
        view.display_message("\033[34mКонтакт успешно создан, нажмите сохранить для добавления в справочник\033[0m")
    else:
        view.display_error(f"\033[34mСоздать контакт не удалось: {reference}\033[0m")
    return reference

# Функция изменения контакта
def update_contact( id: int, record: dict ) -> list:
    reference, status = model.update_reference(id, record)
    if status:
        view.display_message(f"\033[34mКонтак с id {id + 1} успешно обновлен, нажмите сохранить для добавления в справочник\033[0m")
#   else:
#       view.display_error("Ошибка обновления контакта с id {}: элемент не найден".format(id))
    return reference

# Функция удаления контакта по ID
def delete_contact(id: int) -> list:
    reference, status = model.delete_reference(id)
    if status:
        view.display_message(f"\033[34mКонтак с id {id + 1} успешно удален, нажмите сохранить для добавления в справочник\033[0m")
#   else:
#       view.display_error("Ошибка удаления контакта с id {}: элемент не найден".format(id))
    return reference

# Функция нахождения в справочнике контакта по ID
def find_contact_by_id(id: int) -> (id, dict):
    record, status = model.find_record_from_id(id)
    if status:
        view.display_message(f"\033[34mКонтакт с id {id + 1} успешно найден\033[34m")
    else:
        view.display_error(f"\n\033[31mОшибка поиска: контакт не найден\033[30m")
    return id, record

# Функция нахождения в справочнике контакта с указанными параметрами
def find_contact(parameters: dict = {}) -> list:
    reference, status = model.find_records(parameters)
    if status:
        view.display_message("\033[34mКонтакт найден успешно\033[34m")
    else:
        view.display_error(f"\033[31mОшибка поиска контакта с параметрами {parameters}: запись не найдена\033[0m")
    return reference

# Функция обработки ввода команд
def input_handler(inp: int):
    # 3.8 нет поддержки match / case
    if inp == 1:  # Открытие файла
        open_reference( 'test.txt' )
        
    elif inp == 2:  # Сохранение контакта 
        save_reference( 'test.txt', model.reference )
      
    elif inp == 3:  # Вывод всех контактов
        view.show_all( show_contacts(  ) )

    elif inp == 4:  # Добавление контакта
        view.show_all(
            add_contact( view.create_contact() ) )

    elif inp == 5:  # Изменение контакта
        view.show_all( show_contacts(  ) )
        id, rec = view.change_contact( len(model.reference) )
        view.show_all( update_contact( id, rec ) )

    elif inp == 6:  # Удиление контакт по ID
        view.show_all( show_contacts(  ) )
        delete_contact(view.delete_contact(len(model.reference)))

    elif inp == 7: # Поиск контакта по id
        view.show_all( show_contacts(  ) )
        id, rec = find_contact_by_id(view.get_id(len(model.reference)) - 1)
        view.show_contact( id, rec )

    elif inp == 8: # Поиск контакта по параметрам
        view.show_all( show_contacts(  ) )
        rec = view.search_by_parameters( len(model.reference) )
        view.show_all( find_contact( rec ) ) # поиск по параметрам

    elif inp == 0:  # Выход
        if view.exit_program():
            exit()
            
def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
