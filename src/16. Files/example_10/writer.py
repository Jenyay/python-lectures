# Указание кодировки текстового файла

if __name__ == "__main__":
    lines = ["Hello, world!\n" "Привет, мир!\n"]

    with open("example.txt", "wt", encoding="cp1251") as file:
        file.writelines(lines)
