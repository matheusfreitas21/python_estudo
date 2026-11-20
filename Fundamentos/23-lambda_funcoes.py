# Funcao de potencia de um numero

power = lambda num: num ** 2

# Função que verifica se o número e par

is_even = lambda x: x % 2 == 0

# Função que divide um número por outro
div_num = lambda x,y: x / y

# Função que inverte uma string
reverse_string = lambda s: s[::-1]

print(power(5))
print(power(9))
print(is_even(27))
print(is_even(30))
print(div_num(10, 2))
print(div_num(6, 2))
print(reverse_string("Python"))
print(reverse_string("JavaScript"))

# Funcionalidades relacionadas aos filmes 
movies_list =  [
    "Matrix",
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
]
ratings = { 
    "Matrix": [8.5, 9.0, 7.5],
    "Inception": [8.5, 9.0, 7.5],
    "Interstellar": [8.5, 9.0, 7.5],
    "The Dark Knight": [8.5, 9.0, 7.5],
    "Pulp Fiction": [8.5, 9.0, 7.5],

}

# Função para calcular a média de  um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
print(f"Média de Avaliação do filme the Matrix: {average_rating("Matrix")}")

# Função que verifica se um filme esta na lista

check_movie = lambda movie_name: movie_name in movies_list
print(f"Inception está na lista ?: {check_movie("Inception")}")