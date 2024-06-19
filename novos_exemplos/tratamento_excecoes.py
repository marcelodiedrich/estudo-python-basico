# Exemplo de tratamento de exceções em Python
try:
    numero_str = input("Digite um número inteiro: ")
    numero = int(numero_str)
    resultado = 10 / numero
    print(f"O resultado da divisão de 10 por {numero} é: {resultado}")
except ValueError:
    print("Erro: você deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
