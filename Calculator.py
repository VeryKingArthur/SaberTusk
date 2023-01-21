def calculator(expression):
    try:
        return eval(expression)
    except:
        print("Неверное выражение")

x = input("Введите математическое выражение ")
result = calculator(x)
print(result)