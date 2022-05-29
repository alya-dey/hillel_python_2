"""Задача повышенной Интересности. Попробовать посмотреть на написанный код и сделать его более надежным.
Любые изменения приветствуются.
- просмотреть каждую программу и посмотреть как она может упасть. Попробовать ее зафейлить.
- Во время тестирования заметить какие ошибки появляется
- используя исключения изменить код. И не только исключения, а и фантазию."""


def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ZeroDivisionError:
            print("Error! You cannot divide by zero.")
        except ValueError:
            print("Error! You should enter integers, not float or text.")
    return "Calculating finished"


def example2(some_list):
    print("\n\nExample 2")
    sum_of_pairs = []
    for i in range(len(some_list)):
        try:
            sum_of_pairs.append(some_list[i] + some_list[i + 1])
        except IndexError:
            print("Last number has no pair, continuing...")
        except TypeError:
            print("We sum only numbers, continuing...")

    print(f"sum_of_pairs = {sum_of_pairs}")


def printUpperFile(fileName):
    print("\n\nExample 3(printUpperFile)")
    try:
        file = open(fileName, "r")
        for line in file:
            print(line.upper())
        file.close()
    except FileNotFoundError:
        print(f"Sorry, file {fileName} not found.")
        # Если не можем найти файл, предлагаем его создать и все-таки использовать функцию:
        try:
            file = open(fileName, "w")
            file.write(input(f"Please enter your text to create a new file {fileName}: "))
            file = open(fileName, "r")
            printUpperFile(fileName)
            file.close()
        # Если проблема с директорией, то выводим сообщение:
        except FileNotFoundError:
            print("No such directory!")


def main():
    example1()
    some_list = [10, 3, 5, 6, 9, 3]
    example2(some_list)
    example2([10, 3, 5, 6, "NA", 3])
    example2([10, 3, 5, 6])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")


print(main())


