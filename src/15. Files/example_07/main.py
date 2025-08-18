# Демонстрация порционного построчного чтения текстового файла

if __name__ == "__main__":
    file = open("example.txt", "rt")

    while (line := file.readline()) != "":
        print(f"{line=}")

    file.close()
