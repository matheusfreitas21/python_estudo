num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

# Aritmética
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
mod = num1 % num2
exponenciacao = num1 ** num2

print("\n==================================\n")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print(f"Restio da divisão: {num1} mod {num2} é igual a {mod}") 
print(f"Potência: {num1} elevado a {num2} é igual a {exponenciacao}")

#Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print("\n==================================\n")
print(f"{num1} é maior que {num2}? {bigger}")
print(f"{num1} é menor que {num2}? {smaller}")
print(f"{num1} é igual a {num2}? {equal}")
print(f"{num1} é diferente de {num2}? {different}")
print(f"{num1} é maior ou igual a {num2}? {bigger_equal}")
print(f"{num1} é menor ou igual a {num2}? {smaller_equal}")


# Atribuição
num1 += 5 #num1 = num1 + 5
print("\n==================================\n")
print("Novo valor de num1:", num1)
num1 -= 5 #num1 = num1 - 5
print("\n==================================\n")
print("Novo valor de num1:", num1)
num1 *= 5 #num1 = num1 * 5
print("\n==================================\n")
print("Novo valor de num1:", num1)
num1 /= 5 #num1 = num1 / 5 
print("\n==================================\n")
print("Novo valor de num1:", num1)
