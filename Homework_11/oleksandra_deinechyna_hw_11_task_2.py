"""Задача 2. 20 баллов Скинуть файлик с примерами всех конструкций try:except:else:finally
КРОМЕ менеджера контекста. With/as."""


# Example #1
try:
    print("Let\'s divide two numbers!")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = float(a)/float(b)
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except Exception as i:
    print(f"Unexpected error: {i}")
else:
    print(f"Result is {result}")
finally:
    print("End of the operation.\n" + "___"*15)

# Example #2
# Тут программа считает индекс массы тела. Пользователь вводит рост и вес, мы проверяем эти значения и считаем индекс.
# Помимо стандартной ошибки ValueError, когда вместо числа пользователь ввел текст, также создаем свои собственные
# ошибки, которые проверяют, чтобы рост и вес не были отрицательными числами, и чтобы не превышали максимальные
# рост и вес, зафиксированные в мире.

def calculate_bmi(height, weight):
    """calculate body mass index (BMI)"""
    return weight / height**2

def evaluate_bmi(bmi):
    if 18.5 <= bmi < 25:
        return 'healthy'
    if bmi >= 25:
        return 'overweight'
    else:
        return 'underweight'

def bmi():
    try:
        height = float(input("Enter you hight (meters): "))
        weight = float(input("Enter your weight (kilograms): "))
        if height > 3:
            raise Exception("Your height is unreal. Check if you entered meters not centimeters.")
        if weight < 0 or height < 0:
            raise Exception("You cannot enter negative values.")
        if weight > 700:
            raise Exception("Your weight is unreal.")
    except ValueError:
        return "Error! Please enter a valid number."
    except Exception as e:
        return f"Error! {e}"
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)
        return f"Your body mass index is {bmi}, this is considered {evaluation}!"
    finally:
        print("Calculating...")


print(bmi())
