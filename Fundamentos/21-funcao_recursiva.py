# 1 - Fatorial de um numero

def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num -1 ))
number = int(input("Digite o número para o fatorial: \n"))
print(f"O fatorial de {number} é {fatorial(number)}")

# 2 - Soma total de um numero

def total_sum(num):
    if num == 1:
        return 1
    else: 
        return (num + total_sum(num - 1))
num = int(input("Digite o número para soma: \n"))
print((f"A soma total {num} é {fatorial(num)}"))