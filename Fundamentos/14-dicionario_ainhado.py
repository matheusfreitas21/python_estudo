import pprint

filmsDict = {
    "Inception": {
        "director": "Christopher Nolan",
        "imdbRating": 8.8,
        "genre": ["Sci-Fi", "Action", "Thriller"]
    },
    "The Dark Knight": {
        "director": "Christopher Nolan",
        "imdbRating": 9.0,
        "genre": ["Action", "Crime", "Drama"]
    }
}

print(type(filmsDict))  # <class 'dict'>
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(filmsDict)


# 1 - Buscar um informação dentro do dicionário aninhado
print(filmsDict["Inception"]["imdbRating"])  # 8.8

# 2 - Adicionar um item ao dicionário aninhado
filmsDict["Inception"]["year"] = 2010
print(filmsDict)

# 3 - Excluir um item do dicionário aninhado
del filmsDict["The Dark Knight"]
print(filmsDict)    
