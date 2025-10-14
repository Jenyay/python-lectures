# Демонстрация автоматического закрытия файла с помощью оператора with

if __name__ == "__main__":
    lines = ["Hello, world!\n" "Привет, мир!\n", "你好世界!\n"]

    with open("example.txt", "wt") as file:
        file.writelines(lines)

    input("Нажмите Enter...")
