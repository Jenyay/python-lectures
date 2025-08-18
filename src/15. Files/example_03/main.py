# Демонстрация чтения текстового файла в виде одной строки

if __name__ == "__main__":
    file = open("example.txt", "rt")

    text = file.read()
    print(text)

    file.close()
