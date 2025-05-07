import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pyparsing import alphas

df = pd.read_csv(r'clientes-v3-preparado.csv')
print(df.head().to_string())

#histograma
plt.hist(df['salario'])
plt.show()

#histograma - Parâmetro
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de salário')
plt.xlabel('Salario')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequencia')
plt.grid(True)
plt.show()

# Multiplos gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) # 2 linhas, 2 colunas 1 gráfico
# Gráfico de Dispersãp
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salário a Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1, 2, 2) # Linha 1, 2 colunas, 2gráficos
plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha=0.6, s=30) #cor hexadecimal omline
plt.title('Dispersão - Idade e Anos de Experperiencia')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiencia')

# Mapa de calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3) # 1 linhas, 2 colunas, 1 gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salario e Idade')

plt.tight_layout() #ajustar epaçamento
plt.show()
