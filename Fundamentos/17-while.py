# Lista de Filmes
moviesList = [
    "Matrix",
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
]

# 1 - Iterando valores de ma lista de filmes usando while
index = 0

while index < len(moviesList):
    print(f"Filme: {moviesList[index]}")
    index += 1

# 2 - Quando a condicao for atendida, o Loop sera encerrado
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break
    print(f"{moviesList[index]}")
    index += 1
# 3 - Quando a condicao for atendida, o Loop sera pulado e continuara a execucao
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        index += 1
        continue
    print(f"{moviesList[index]}")
    index += 1
# 4 - Avaliando do Filme com While
movieName = input("Digite o nome do filme: \n")
movieRating = float(input("Digite a nota do filme: \n"))
totalRating = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    count += 1

if movieRating > 0:
    avarage = total / movieRating
else:
    avarage = 0
print(f"Media de avaliacao do filme {movieName} é: {avarage:.2f}")
