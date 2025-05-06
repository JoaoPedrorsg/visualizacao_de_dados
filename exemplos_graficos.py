import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv(r'C:\Users\joaoz\OneDrive\Documentos\clientes-v3-preparado.csv')

df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
# Heatmap de correlção
plt.figure(figsize=(10, 6))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de calor da Correlação entre Variáveis')
plt.show()

# Já usei
# Countplot
sns.countplot(x='estado_civil', data=df)
plt.title('Distribuição do Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.show()

# Countplot com legenda
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df)
plt.title('Distribuição do Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nivel de Educação')
plt.show(),
