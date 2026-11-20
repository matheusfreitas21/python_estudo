name = input("Digite o nome do filme: \n")
year_launch = int(input("Digite o ano de lançamento do filme: \n"))
noteMovie = float(input("Digite a nota do filme: \n"))


print("Dados do Filme")
print("==================================")
#ALernativa 1
print("Filme:", name)
print("Ano de Lançamento:", year_launch)
print("Filme: " + name)

print("\n==================================\n")
#ALernativa 2
print("Nome do Filme:", name, "\nAno de Lançamento:", year_launch, "\nNota do Filme:", noteMovie)

print("\n==================================\n")
#Alternativa 3
print(f"Filme: {name} \nAno de Lançamento: {year_launch} \nNota do Filme: {noteMovie}")