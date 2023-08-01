'''
Elabore um programa que pergunte ao aluno suas 3 notas escolares.
O programa deverá calcular a média dos 3 alunos inseridos e exibir esta média.
'''

# Etapa 1: entrada de dados
nota1 = float(input("Informe sua primeira nota 1: "))
nota2 = float(input("Informe sua segunda nota 2: "))
nota3 = float(input("Informe sua terceira nota 3: "))

# Etapa 2: processamento de dados
media = (nota1 + nota2 + nota3) / 3

# Etapa 3: Saída de dados (resposta na tela)
print("Sua média é", media)