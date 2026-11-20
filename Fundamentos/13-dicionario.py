filmInception = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "imdbRating": 8.8,
    "genre": ["Sci-Fi", "Action", "Thriller"],
}

print(type(filmInception))  # <class 'dict'>
print(len(filmInception))  # 4
print(filmInception)


# 1 - Recuperar um elemento do dicionário
print(filmInception["genre"])
print(filmInception.get("director"))

#2 - Buscar apenas a chave do dicionário
print(filmInception.keys())

# 3 - Buscar apenas os valores do dicionario
print(filmInception.values())

# 4 - Buscar itens do dicionário com chave e valor
print(filmInception.items())

# 5 - Adicionar um item ao dicionário
filmInception["director"] = "Christopher Nolan"
print(filmInception)

# 6 - Atualizar um item do dicionário
filmInception.update({"imdbRating": 9.0})
print(filmInception)

# 7 - Remover um item do dicionário
filmInception.pop("director")
print(filmInception)