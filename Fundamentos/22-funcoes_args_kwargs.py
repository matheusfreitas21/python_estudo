# 1 - Soma de números 

def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

sum(7)
sum(7, 9)
sum(7, 9, 10, 11)
sum(7, 10,9,8,7,6)

#2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de Cursos:")
presentation(nome="Python", category="Backend", level="Iniciante")
presentation(nome="Visão computacional com Python", category="IA", level="Avançado")
presentation(nome="Dashboards com Dash", category="Data Science", level="Intermediário")