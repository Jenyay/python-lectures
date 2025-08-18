# Ошибка указания неправильной кодировки файла при кодировании

if __name__ == "__main__":
    text = "\n".join(["Hello, world!", "Привет, мир!", "你好世界!"])
    data_bytes = text.encode("cp1251")
