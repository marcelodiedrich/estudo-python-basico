# Exemplo de manipulação de data e hora em Python
from datetime import datetime, timedelta

# Obtendo a data atual
data_atual = datetime.now()
print("Data atual:", data_atual)

# Adicionando dias a uma data
data_futura = data_atual + timedelta(days=7)
print("Data daqui a 7 dias:", data_futura)

# Formatando a data como string
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", data_formatada)
