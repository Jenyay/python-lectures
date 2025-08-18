if __name__ == "__main__":
    file = open("example.txt", "wt")

    print(type(file))
    print(dir(file))

    file.close()
