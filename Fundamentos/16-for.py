# Lista de Filmes
moviesList = [
    "Matrix",
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
]

for movie in moviesList:
    print(f"Filme: {movie}")


# 2 - Quando a condicao dor atendidam o Loop sertá encerrado 
for movie in moviesList:
    if movie == "Inception":
        break
    else:
        print(f"{movie}")

# 3 - Quando a condicao for atendida, o Loop sera pulado e continuara a execucao
for movie in moviesList:
    if movie == "Inception":
        continue
    print(f"{movie}")

# 4 - Avaliando o indice do item da lista
movieName - inout("Digite o nome do filme: \n")
movieRanting = float(input("Digite a nota do filme: \n"))

total = 0 
for i  in range(movieRanting):
    note = float (input(f"Digite a nota do filme {movieName} na {i}ª avaliação: \n"))
    total += note
if movieRanting > 0:
    average = total / movieRanting
else:
    average = 0
print(f"A média das notas do filme {movieName} é: {average:.2f}")

