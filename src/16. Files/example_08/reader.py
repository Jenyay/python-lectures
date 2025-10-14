# Демонстрация одновременного открытия файла разными скриптами

if __name__ == "__main__":
    file = open("example.txt", "rt")

    lines = file.readlines()
    print(f"{lines=}")

    input("Нажмите Enter...")

    file.close()
