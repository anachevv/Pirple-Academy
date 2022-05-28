import os


def NoteTaking():
    print("Starting to take a note.")
    askFilename()


def askFilename():
    file_name = input("Please enter the file name:\n")
    file_path = "./" + file_name + ".txt"
    if fileExists(file_path):
        askFileMode(file_path)
    else:
        askFileInput(file_path)


def fileExists(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    return False


def askFileInput(file_path):
    txt = input("Please write down the content:\n")
    writeToFile(file_path, txt + "\n")
    print("Content written...")


def askFileMode(file_path):
    choice = input(
        "\nWhat do you want to do? Enter the number against the choice.\n1 Read the file\n2 Delete the file and start over\n3 Append the file: \n\n")
    if choice == "1":
        txt = readFile(file_path)
        print("Your file")
        print(txt)

    elif choice == "2":
        deleteFile(file_path)
        createEmptyFile(file_path)
        print("File is deleted and empty one is made on its place.")
    elif choice == "3":
        txt = input("Please enter the content, you want to add:\n\n")
        appendToFile(file_path, txt)
        print("Content added!")


def writeToFile(file_path, content):
    file = open(file_path, "w")
    file.write(content)
    file.close()


def readFile(file_path):
    content = ""
    with open(file_path, "r") as file:
        for line in file:
            content = content + line
    return content


def appendToFile(file_path, txt):
    file = open(file_path, "a")
    file.write(txt)
    file.close()


def deleteFile(file_path):
    os.remove(file_path)


def createEmptyFile(file_path):
    file = open(file_path, "w")
    file.close()


NoteTaking()
