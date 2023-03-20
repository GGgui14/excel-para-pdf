import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo Excel
df = pd.read_excel('entrada.xlsx')

# Criação do gráfico
fig, ax = plt.subplots()
ax.plot(df['coluna1'], df['coluna2'])

# Salva a imagem em formato PNG
fig.savefig('saida.png')
