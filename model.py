from os.path import isfile
from random import choice, randrange


# #
# Заметки:
# 1. Status операции как и код ошибки отдавать 1-м, для простоты обработки, чтобы не путаться...
# 2.
#
# Не реализовано:
# 1. Проверка открытали книга... или мы работаем с объектов в памяти...
# #


__firstnames  = ["Андрей", "Антон", "Артем", "Дмитрий", "Тимофей", "Павел", "Максим", "Кирил", "Сергей", "Иван", "Петр", "Егор", "Владимир"]
__lastnames   = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Большаков", "Умнов"]
__comments    = ["Рабочий", "Мобильный", "Домашний", "Дополнительный"]
__phone_codes = [301, 302, 336, 341, 342, 343, 345, 346, 347, 349, 351, 352, 353, 365, 381, 382, 383, 384, 385, 388, 390, 391, 394, 395] + \
[401, 411, 413, 415, 416, 421, 423, 424, 426, 427, 471, 472, 473, 474, 475, 481, 482, 483, 484, 485, 486, 487, 491, 492, 493, 494, 495, 496, 498, 499] + \
[811, 812, 813, 814, 815, 816, 817, 818, 820, 821, 831, 833, 834, 835, 836, 841, 842, 843, 844, 845, 846, 847, 848, 851, 855, 861, 862, 863, 865, 866, 867, 869, 871, 872, 873, 877, 878, 879] + \
[900, 901, 902, 903, 904, 905, 906, 907, 908, 909] + \
[910, 911, 912, 913, 914, 915, 916, 917, 918, 919] + \
[920, 921, 922, 923, 924, 925, 926, 927, 928, 929] + \
[930, 931, 932, 933, 934, 935, 936, 937, 938, 939] + \
[940, 941, 942, 943, 944, 945, 946, 947, 948, 949] + \
[950, 951, 952, 953, 954, 955, 956, 957, 958, 959] + \
[960, 961, 962, 963, 964, 965, 966, 967, 968, 969] + \
[970, 971, 972, 973, 974, 975, 976, 977, 978, 979] + \
[980, 981, 982, 983, 984, 985, 986, 987, 988, 989] + \
[990, 991, 992, 993, 994, 995, 996, 997, 998, 999]


# Global
reference = []
imaginary_friends = []


def generate_reference( count: int = 10 ) -> ( list, bool ):
    global imaginary_friends
    result_list = []

    for _ in range(count):
        result_list.append( {
            "lastname":  choice( __lastnames ),
            "firstname": choice( __firstnames ),
            "phone":      f"+7-{ choice(__phone_codes) }-{ randrange( 1000 ) }-{ randrange( 100 ) }-{ randrange( 100 ) }",
            "comment":    choice( __comments )
        } )
    imaginary_friends = result_list
    return imaginary_friends, True
# print( *generate_reference()[ 0 ], sep="\n" )


def read_reference_from_file( file_name: str = "test.txt" ) -> ( list, bool ):
    global reference

    return_list = []
    status = False
    try:
        if isfile( file_name ):
            with open( file_name, encoding='UTF-8' ) as file:
                for line in file:
                    if line != "":
                        record = line.strip().split(";")
                        return_list.append( {
                            "lastname":  record[0].strip(),
                            "firstname": record[1].strip(),
                            "phone":      record[2].strip(),
                            "comment":    record[3].strip()
                        } )
            status = True
        else:
            if write_reference_from_file( file_name ):
                status = read_reference_from_file( file_name )[1]
    except:
        return reference, status

    reference = return_list
    return reference, status
# print( *read_reference_from_file()[ 0 ], sep="\n" )
# print( read_reference_from_file()[ 1 ], sep="\n" )


def write_reference_from_file( file_name: str = "test.txt", reference: list = reference ) -> bool:
    try:
        with open( file_name, "w", encoding='UTF-8' ) as file:
            for dt in reference:
                file.write( f"{';'.join( dt.values() ) }\n" )
        return True

    except:
        return False
# print( read_reference_from_file()[ 1 ], sep="\n" )
# print( write_reference_from_file( reference = generate_reference()[0] ) )


def get_reference( count: int = 0 ) -> ( list, bool ):
    result_list = []
    status = False
    if count > 0:
        if count + 1 > len( reference ):
            result_list += reference[:len( reference )]
        else:
            result_list += reference[:count]
            status = True
    elif count == 0:
        return reference[:], True

    return result_list, status
# print( read_reference_from_file()[ 1 ], sep="\n" )
# print( *get_reference( 100 )[0], sep="\n" )


def add_reference( record: dict ) -> ( list, bool ):
    global reference
    reference_len = len( reference )
    reference.append( record )

    if reference_len < len( reference ):
        return reference, True
    return reference, False
# print( read_reference_from_file()[ 1 ], sep="\n" )
# print( add_reference( generate_reference( 1 ) ) )


def delete_reference( id: int ) -> ( list, bool ):
    global reference

    if 0 <= id and id <= len( reference ) - 1:
        del reference[ id ]
        return reference, True
    return reference, False
# print( read_reference_from_file()[ 1 ], sep="\n" )
# print( delete_reference( 11 )[1] )


def update_reference( id: int, record: dict ) -> ( list, bool ):
    global reference
    keys = ['lastname', 'firstname', 'phone', 'comment']

    if 0 <= id and id <= len( reference ) - 1:
        for key, value in record.items():
            if key in keys:
                reference[ id ][ key ] = record[ key ]
        return reference, True
    return reference, False
# print( read_reference_from_file()[ 1 ], sep="\n" )
# print( update_reference( 11, {'last_name': 'Петров', 'first_name': 'Егор', 'phone': '+7-811-115-41-21', 'comment': 'Мобильный'} )[1] )


def find_records( parameters: dict = {} ) -> ( list, bool ):
    global reference
    result_list = reference[:]

    keys = ['lastname', 'firstname', 'phone', 'comment']

    for key, value in parameters.items():
        if key in keys:
            result_list = list(filter(lambda el: el[key] == value, reference))
        else:
            pass

    status = False if len( result_list ) == 0 else True
    return result_list, status
# print( read_reference_from_file()[ 1 ], sep="\n" )
# print( *find_records({'last_name': 'Кузнецов'})[ 0 ], sep="\n" )


def find_record_from_id( id: int ) -> ( list, bool ):
    global reference

    if 0 <= id and id <= len( reference ) - 1:
        return reference[ id ], True
    else:
        return {}, False
# print( read_reference_from_file()[ 1 ], sep="\n" )
# print( *find_record_from_id( 1 )[ 0 ], sep="\n" )