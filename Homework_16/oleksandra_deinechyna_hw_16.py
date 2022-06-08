import sys
import ast


def read_data():
    """Open file with data in dict format"""
    with open("exchange_data.txt", "r") as file:
        data: str = file.read()
        data_eval: dict = ast.literal_eval(data)
    return data_eval


def update_data():
    """Updates data in file after converting"""
    with open("exchange_data.txt", "w") as file:
        file.write(str(currency_data))


def exchanger():
    """Can show UAH, USD rates read from file, convert UAH or USD from balance and update balance"""

    print("Welcome to exchange program! Use commands: COURSE USD, COURSE UAH, EXCHANGE UAH X, EXCHANGE USD X, STOP")
    while True:
        command: str = input('COMMAND?\n')
        command_split: list = command.split()

        if command_split[0] == 'COURSE':
            if command_split[1] == 'USD':
                print(f'RATE {currency_data["USD_rate"]}, AVAILABLE {currency_data["USD_available"]}')
                continue
            elif command_split[1] == 'UAH':
                print(f'RATE {currency_data["UAH_rate"]}, AVAILABLE {currency_data["UAH_available"]}')
                continue
            else:
                print(f'INVALID CURRENCY {command_split[1]}')
                continue

        elif command_split[0] == 'EXCHANGE':
            try:
                if command_split[1] == 'USD':
                    usd_to_uah: float = float(command_split[2])/currency_data["UAH_rate"]
                    if usd_to_uah > currency_data["UAH_available"]:
                        print(f'UNAVAILABLE, REQUIRED BALANCE UAH {usd_to_uah}, '
                              f'AVAILABLE {currency_data["UAH_available"]}')
                    else:
                        print(f'UAH {usd_to_uah}, RATE {currency_data["UAH_rate"]}')
                        currency_data["UAH_available"] -= usd_to_uah
                        currency_data["USD_available"] += float(command_split[2])
                        update_data()
                    continue

                elif command_split[1] == 'UAH':
                    uah_to_usd: float = float(command_split[2]) / currency_data["USD_rate"]
                    if uah_to_usd > currency_data["USD_available"]:
                        print(f'UNAVAILABLE, REQUIRED BALANCE USD {uah_to_usd}, '
                              f'AVAILABLE {currency_data["USD_available"]}')
                    else:
                        print(f'USD {uah_to_usd}, RATE {currency_data["USD_rate"]}')
                        currency_data["USD_available"] -= uah_to_usd
                        currency_data["UAH_available"] += float(command_split[2])
                        update_data()
                    continue

                else:
                    print(f'INVALID CURRENCY {command_split[1]}')
                    continue

            except IndexError:
                print('YOU HAVEN\'T PUT THE AMOUNT OF CURRENCY')
                continue

        elif command_split[0] == 'STOP':
            print('SERVICE STOPPED')
            sys.exit()  # exit program

        else:
            print('UNKNOWN COMMAND')


currency_data: dict = read_data()

if __name__ == '__main__':
    print(exchanger())


# currency_data = {"USD_available": 13500.0, "UAH_available": 39000.0, "USD_rate": 27.3, "UAH_rate": 0.036363}

"""
Задача №4 Обменник USD-UAH (система учета для кассира)
Сложность 4/4

Реализовать функционал обменника USD и UAH валют посредством Python.
User Story: После запуска файла пользователь отдает команду на
    - получение курса и остатков
       COURSE USD
       - система проверяет доступость валюты, ее курс и остаток  
      
       COMMAND?
       >>> COURSE USD
       RATE 27.5, AVAILABLE 13500.98
      
       COMMAND?
       >>> COURSE UAH
       RATE 27.3, AVAILABLE 39345.5
      
       COMMAND?
       >>> COURSE BCH
       INVALID CURRENCY BCH
   
    - обмен
       EXCHANGE UAH 100
       - система проверяет дотупно ли нужное количество USD в соответствии с курсом, если количество доступно - поизводит обмен и обновляет баллансы
      
       COMMAND?
       >>> EXCHANGE UAH 100
       USD 3.6363, RATE 0.036363
      
       EXCHANGE USD 100
       - система проверяет дотупно ли нужное количество UAH в соответствии с курсом, если количество доступно - поизводит обмен и обновляет баллансы
      
       COMMAND?
       >>> EXCHANGE USD 100
       UAH 2730, RATE 27.3
      
       - если баланса валюты недостаточно
       COMMAND?
       >>> EXCHANGE USD 2000
       UNAVAILABLE, REQUIRED BALANCE UAH 54600, AVAILABLE 39345.5
  
    - остановку сервиса
       STOP
       - программа завершается
   
       COMMAND?
       >>> STOP
       SERVICE STOPPED
      
Tech Requirements:
Ввод данных с помощью функции input.
Состояние системы (курс и доступный баланс для каждой валюты) считывается и хранится в отдельном
файле (формат файла не усмотрение разработчика).
"""