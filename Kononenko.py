class InvalidDataError(Exception):
    pass


def validate_data(data):
    fields = data.split()
    if len(fields) != 5:
        raise InvalidDataError("Неверное количество полей")
    
    last_name, first_name, middle_name, dob, phone, gender = fields
    
    # Проверка формата данных
    if not last_name or not first_name or not middle_name:
        raise InvalidDataError("Не введены ФИО")
    if len(dob) != 10 or dob.count(".") != 2:
        raise InvalidDataError("Неверный формат даты рождения")
    if not phone.isdigit():
        raise InvalidDataError("Неверный формат номера телефона")
    if gender not in ["f", "m"]:
        raise InvalidDataError("Неверный формат пола")
    
    # Запись данных в файл
    filename = f"{last_name}.txt"
    data_line = f"{last_name} {first_name} {middle_name} {dob} {phone} {gender}"
    
    try:
        with open(filename, "a") as file:
            file.write(data_line + "\n")
    except IOError as e:
        raise e


def main():
    try:
        input_data = input("Введите данные: ")
        validate_data(input_data)
        print("Данные успешно сохранены!")
    except InvalidDataError as e:
        print(f"Ошибка: {str(e)}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    main()
