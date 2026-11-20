filmsSet = {
    "Matrix",
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
}

print(type(filmsSet))  # <class 'set'>


# 1 - Buscar o tamanho do set
print(len(filmsSet))

#2 - True e 1 são considerados o memso valor

exampleSet = {"Inception", True, 1, 8.7}
print(exampleSet)  # {'Inception', True, 8.7}

# 3 - Adicionar um item  de outro set
filmsSet.update(exampleSet)
print(filmsSet) 

# 4 - Remover um item do set
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)  # {'Inception', 'Matrix', 'Interstellar',