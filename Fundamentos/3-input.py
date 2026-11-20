name = input("Digite o nome do filme: \n")
year_launch = int(input("Digite o ano de lançamento do filme: \n"))
noteMovie = float(input("Digite a nota do filme: \n"))
planIncluded = bool(input("O filme está no plano incluído? (True/False): \n"))

print("Filme:", name)
print("Ano de Lançamento:", year_launch)
print("Nota do Filme:", noteMovie)
print("Plano Incluído:", planIncluded)

print(type(name))
print(type(year_launch))
print(type(noteMovie))
print(type(planIncluded))