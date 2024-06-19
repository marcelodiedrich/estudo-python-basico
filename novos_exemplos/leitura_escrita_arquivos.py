# Exemplo de leitura e escrita de arquivos em Python
# Escrevendo em um arquivo
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Este é um exemplo de texto que será escrito no arquivo.")

# Lendo o arquivo
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
