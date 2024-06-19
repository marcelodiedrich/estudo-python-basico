# Exemplo de definição e chamada de função em Python
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

notas_aluno = [7.5, 8.0, 9.5, 6.0, 8.5]
media_aluno = calcular_media(notas_aluno)
print(f"A média do aluno é: {media_aluno}")
