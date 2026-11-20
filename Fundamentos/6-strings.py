movieName = "The Matrix"
movieName2 = "the matrix"

print(movieName == movieName2)  # False, because of case sensitivity
movieDescription = """
    A computer hacker
    learns about the true nature of his 
    reality and his role in the war against its controllers.
"""
print(movieName)
" 1- Multiplicacao de strings"
line = "="
print(line * 50)
print(movieDescription)

# 2- Procurando por uma substring dentro de uma string
print("Matrix" in movieName)  # True
print("acao" in movieName)  # False