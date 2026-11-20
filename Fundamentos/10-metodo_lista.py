filmsList = [
    "Matrix",
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
]

# 1 - Tamanho da lista
print(len(filmsList))

# 2 - Recuperar um item da lista pelo nome
print(filmsList.index("Inception"))

# 3 - Adicionar item ao final da lista
filmsList.append("The Godfather")
print(filmsList)

# 4 - Orgenar a lista em ordem alfabética
filmsList.sort()
print(filmsList)

# 5 - Copiar os items de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Inception")
print(filmsCopy)

# 6 - Limpar a lista
filmsCopy.clear()
print(filmsCopy)

