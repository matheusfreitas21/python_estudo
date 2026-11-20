name = input("Digite seu nome filme: \n")
yearRelease = int(input("Digite o ano de lançamento do filme: \n"))
rating = float(input("Digite a nota do filme: "))


# verifica se o filme e recomendado
if rating > 8.0 and yearRelease > 2015:
    print(f"{name} é um filme recomendado!")
else:
    print(f"{name} não é um filme recomendado!")


num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))
operation = input("Digite a operação desejada (+, -, *, /): \n")

if operation == "+":
    result = num1 + num2
    print(f"O resultado da soma é: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"O resultado da subtração é: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"O resultado da multiplicação é: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        result = 0
    print(f"O resultado da divisão é: {result}")
else:
    print("Operação inválida!") 