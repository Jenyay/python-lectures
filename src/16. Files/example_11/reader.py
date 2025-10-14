# Ошибка указания неправильной кодировки файла при чтении

if __name__ == "__main__":
    with open("example.txt", "rt", encoding="cp1251") as file:
        lines = file.readlines()

    print(f"{lines=}")
