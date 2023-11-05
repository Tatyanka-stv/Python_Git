import os

def path_to_file():#функція призначена для пошуку файлу students.txt: чи існує файл взагалі і якщо файл існує тоді надається шлях до нього
    try:
        current_directory = os.getcwd() # шукаємо поточну директорію
        #print('Поточна директорія: ', current_directory)
        start_dir = current_directory
        target_file = 'students.txt'  # Имя файла, який ми шукаємо
        file_paths = [] # Створюємо список для зберігнання шляхів до файлу

        for root, dirs, files in os.walk(start_dir):
            if target_file in files:
                file_path = os.path.join(root, target_file)
                file_paths.append(file_path)

        if file_paths:
            print('Файл ' + str(target_file) + ' знайдено за наступними шляхами: ')
            for file_path in file_paths:
                print(file_path)
            return file_paths[0]
        else:
            print('Файл ' + str(target_file) +' не знайдено.\n')   
            return None
    except:
        print('Файл не знайдений.\n')   

def read_students(file_path):
    students = []
    if file_path is not None:
        with open(file_path, "r") as file:
            for line in file:
                student_data = line.strip().split(',')
                students.append(student_data)
             
    return students

def save_students(file_path, students):
    with open(file_path, "w") as file:
        for student in students:
            file.write(','.join(student) + '\n')
           


def is_valid_name(name):
    allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдежзийклмнопрстуфхцчшщьыъэюяЁёІіЇї")
    for char in name:
        if char not in allowed_characters:
            return False
    return True

def is_valid_grade(grade):
    try:
        grade = float(grade)
        if (0 <= grade) and (grade <= 12):
            return True
        else:
            print('Ви ввели невірне значення середнього балу.')
    except ValueError:
        print('Введене значення недопустиме для середнього балу.')
    return False


def add_student(file_path, students):
    print()
    last_name = input('Прізвище студента: ')
    while not is_valid_name(last_name):
        print('Прізвище введено невірно. Воно містить не лише букви.')
        last_name = input('Прізвище студента: ')

    first_name = input("Ім'я студента: ")
    while not is_valid_name(first_name):
        print("Ім'я введено невірно. Воно містить не лише букви.")
        first_name = input("Ім'я студента: ")

    while True:
        average_grade = input('Середній бал (0-12): ')
        if is_valid_grade(average_grade):
            break
    student_id = str(len(students) + 1)
    student_data = [student_id, last_name, first_name, average_grade]
    students.append(student_data)
    save_students(file_path, students)
    print('\nСтудента додано. ID студента:', student_id)

def remove_student(file_path, students):
    last_name = input('Введіть прізвище студента, якого бажаєте видалити: ')
    flag_is_student_in_file = False
    for student in students:
        if student[1] == last_name:
            students.remove(student)
            save_students(file_path, students)
            flag_is_student_in_file = True
            print('Студента з ID: '+student[0]+' Прізвище: '+student[1]+' зі списку видалено.')
            break
    if not flag_is_student_in_file:
        print('Студента з прізвищем', last_name, 'не знайдено.')

def change_student_info(file_path, students):
    last_name = input('Введіть прізвище студента, інформацію про якого ви бажаєте змінити: ')
    flag_is_student_in_file = False
    for student in students:
        if student[1] == last_name:

            first_name = input("Нове ім'я студента (введіть нове ім'я або натисніть Enter, щоб залишити попереднє ім'я без змін): ")
            while not is_valid_name(first_name):
                print("Ім'я введено невірно. Воно містить не лише букви.")
                first_name = input("Ім'я студента: ")
            if first_name:
                student[2] = first_name

            average_grade = input('Новий середній бал (введіть нове значення або натисніть Enter, щоб залишити попереднє значення без змін): ')
            if average_grade:
                while not is_valid_grade(average_grade):
                    average_grade = input('Введіть новий середній бал.')
                student[3] = average_grade

            new_last_name = input('Змінити прізвище студента? (введіть нове прізвище або натисніть Enter, щоб залишити попереднє прізвище без змін): ')
            while not is_valid_name(new_last_name):
                print("Прізвище введено невірно. Воно містить не лише букви.")
                first_name = input("Прізвище студента: ")
            if new_last_name:
                student[1] = new_last_name
            save_students(file_path, students)
            flag_is_student_in_file = True
            print('Інформацію про студента оновлено.')
            break
    if not flag_is_student_in_file:
        print('Студента з прізвищем ', last_name, ' не знайдено.')

def show_all_students(students):
    if len(students) > 0:
        print('Список студентів:')
        print()
        for student in students:
                print(student[0]+'. '+student[1]+' '+student[2]+', середній бал: '+student[3])
        print()
    else:
        print('У списку немає жодного студента.')

def search_student(students):
    print("Пошук студентів за завданими параметрами:\n1. ID\n2. Прізвище\n3. Ім'я\n4. Середній бал:\n ")
    choice_parameter = input("Введіть параметру пошуку (1-4): ")
    flag_is_student_in_file = False

    if choice_parameter == '1':
        search_parameter = input('Введіть для пошуку ID студента: ')
        for student in students:
            if search_parameter == student[0]:
                print('ID: '+student[0]+' Прізвище: '+student[1]+" Ім'я: "+student[2]+' Середній бал: '+student[3])
                flag_is_student_in_file = True

    if choice_parameter == '2':
        search_parameter = input('Введіть для пошуку прізвище студента: ')
        for student in students:
            if search_parameter == student[1]:
                print('ID: '+student[0]+' Прізвище: '+student[1]+" Ім'я: "+student[2]+' Середній бал: '+student[3])
                flag_is_student_in_file = True

    if choice_parameter == '3':
        search_parameter = input("Введіть для пошуку ім'я студента: ")
        for student in students:
            if search_parameter == student[2]:
                print('ID: '+student[0]+' Прізвище: '+student[1]+" Ім'я: "+student[2]+' Середній бал: '+student[3])
                flag_is_student_in_file = True

    if choice_parameter == '4':
        search_parameter = input('Введіть для пошуку середній бал студента: ')
        for student in students:
            if search_parameter == student[3]:
                print('ID: '+student[0]+' Прізвище: '+student[1]+" Ім'я: "+student[2]+' Середній бал: '+student[3])
                flag_is_student_in_file = True

    if not flag_is_student_in_file:
        print('Студентів із завданим параметром не знайдено.')



def sort_students(students):
    print('Сортування студентів за завданими параметрами:')
    print('1. За ID')
    print('2. За прізвищем')
    print("3. За ім'ям")
    print('4. За середнім балом')
    sort_parameter = input('Введіть параметр сортування (1-4): ')
    if sort_parameter == '1':
        students.sort(key=lambda student: int(student[0])  if 1 <= int(student[0]) < 10 else 0)
        students.sort(key=lambda student: int(student[0])  if int(student[0]) >= 10 else 0)
    else:
        if sort_parameter == '2':
            students.sort(key=lambda student: student[1])
        else:
            if sort_parameter == '3':
                students.sort(key=lambda student: student[2])
            else:
                if sort_parameter == '4':
                    students.sort(key=lambda student: float(student[3]), reverse=True)
                else:
                    print('Ви ввели неправильний параметр сортування.')
                    return

    show_all_students(students)

def excellent_students(students):
    excellent = [student for student in students if float(student[3]) >= 10]
    if len(excellent) > 0:
        print("Список 'відмінників':")
        show_all_students(excellent)
    else:
        print('Відмінники відсутні.')

def is_excellent(average_grade):
    try:
        grade = float(average_grade)
        return grade >= 10
    except ValueError:
        return False

def validate_choice(options):
    while True:
        options_str = ', '.join(options)
        choice = input('Оберіть дію '+options_str+' : ')
        if choice in options:
            return choice
        else:
            print('Ви зробили неправильний вибір. Будь ласка, оберіть із доступних опцій.')

def check_is_file_opening():
    file_path = path_to_file()
    # перевіряємо чи відкритий файл
    try:
        with open(file_path, 'r') as file:
        # якщо файл відкритий, то він автоматично буде закритий при виході з блоку 'with'
                #print('Файл '+str(file_path)+' відкритий.") #це перевірочний надпис
            file.close()
            #print('Файл '+str(file_path)+' закритий.') #це перевірочний надпис
        
    except PermissionError:
        print('Файл ' + str(file_path) + ' заблокований іншим процесом.')
    # якщо  файл заблокований іншим процесом, то його можна спробувати закрити
        try:
            os.fsync(file.fileno())  # примусово синхронизуємо буфери та закриваємо файл
            file.close()
            print(f"Файл '{file_path}' успешно закрыт.")
        except Exception as e:
            print('Не вдалося закрити файл '+str(file_path))


def exit_program(file_path, students):
    while True:
        choice = input('Виберіть, як завершити роботу:\n1. Завершити роботу та зберегти зміни в файлі\n2. Завершити роботу та видалити файл\n')
        if choice == '1':
            save_students(file_path, students)
            check_is_file_opening()
            print("Файл змінено. Вихід з програми.")
            exit(0)
        elif choice == '2':
            check_is_file_opening()
            os.remove(file_path)
            print("Файл видалено. Вихід з програми.")
            exit(0)
        else:
            print("Неправильний вибір. Будь ласка, оберіть 1 або 2.")
       
#ПОЧАТОК ОСНОВНОЇ ЧАСТИНИ:

print('\nПрограма опрацювання списку студентів.\n')

file_path = path_to_file()

while True:
    print('Робота з файлом.')
    print("1. Створити файл")
    print("2. Відкрити файл")
    print("3. Вийти")
    menu_choice = validate_choice(["1", "2", "3"])
    
    if menu_choice == '1':
        if file_path is None:#якщо файла students.txt не існує, то ми його створюємо, визначаємо його шлях через функцію path_to_file()
            with open("students.txt", "w") as file:
                print("\nФайл для студентів створено.\n")
                file_path = path_to_file()
                students = []
                while True:
                    print('\nПрацюємо зі списком студентів.')
                    print("1. Додати студента")
                    print("2. Видалити студента")
                    print("3. Змінити інформацію про студента")
                    print("4. Показати на екрані ВСІХ студентів")
                    print("5. Вивести на екран інформацію про студента, виконавши пошук за вказаним параметром")
                    print("6. Вивести студентів в певному порядку")
                    print("7. Вивести 'відмінників'")
                    print("8. Завершити роботу")
                    choice = validate_choice(["1", "2", "3", "4", "5", "6", "7", "8"])
                    if choice == '1':
                        add_student(file_path, students)
                    elif choice == '2':
                        remove_student(file_path, students)
                    elif choice == '3':
                        change_student_info(file_path, students)
                    elif choice == '4':
                        show_all_students(students)
                    elif choice == '5':
                        search_student(students)
                    elif choice == '6':
                        sort_students(students)
                    elif choice == '7':
                        excellent_students(students)
                    elif choice == '8':
                        exit_program(file_path,students)
                        break

        else:
            print("Файл вже існує. Оберіть 'Відкрити файл' або 'Вийти'.")


    elif menu_choice == '2':
        if file_path is not None:
            students = read_students(file_path)
            while True:
                print("1. Додати студента")
                print("2. Видалити студента")
                print("3. Змінити інформацію про студента")
                print("4. Показати на екрані ВСІХ студентів")
                print("5. Вивести на екран інформацію про студента, виконавши пошук за вказаним параметром")
                print("6. Вивести студентів в певному порядку")
                print("7. Вивести 'відмінників'")
                print("8. Завершити роботу")
                choice = validate_choice(["1", "2", "3", "4", "5", "6", "7", "8"])
                if choice == '1':
                    add_student(file_path, students)
                elif choice == '2':
                    remove_student(file_path, students)
                elif choice == '3':
                    change_student_info(file_path, students)
                elif choice == '4':
                    show_all_students(students)
                elif choice == '5':
                    search_student(students)
                elif choice == '6':
                    sort_students(students)
                elif choice == '7':
                    excellent_students(students)
                elif choice == '8':
                    exit_program(file_path,students)
                    break
        else:
            print("Файл не існує. Спершу створіть файл ('Створити файл для студентів').")
    elif menu_choice == '3':
        print("Вихід з програми.")
        break        
