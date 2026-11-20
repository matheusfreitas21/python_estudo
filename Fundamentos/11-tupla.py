filmsTuple = (
    "Matrix",
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
)

print(type(filmsTuple))  # <class 'tuple'>

# 1 - Buscar os dois primeiros itens da tupla
print(filmsTuple[:2])

# 2 - Buscar o ultimo itens da tupla
print(filmsTuple[-1])

# 3 - Busca filmes ate uma determinada posição
print(filmsTuple[:3])

# 4 -  Buscar filmes de uam posição em diante
print(filmsTuple[2:])

# 5 - Recuperar um item da tupla pelo nome
print(filmsTuple.index("Inception"))