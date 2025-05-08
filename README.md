# Análise de Dados de Clientes

Este projeto realiza uma análise exploratória do dataset `clientes-v3-preparado.csv`, utilizando bibliotecas como **Matplotlib** e **Seaborn**. O objetivo é entender a distribuição de salários, escolaridade, idade e experiência dos clientes.

## 🔍 Visão Geral

Foram gerados diversos gráficos para análise estatística e visual:

- Histogramas de salário
- Gráficos de dispersão entre idade, salário e experiência
- Mapas de calor de correlação entre variáveis
- Gráficos de barras e pizza para distribuição de escolaridade
- Gráficos de densidade, regressão e pairplot
- Countplots com agrupamentos por estado civil e nível educacional

---

## 📁 Estrutura do Projeto

<pre><code>📂 intro_visualizacao
├── intro_visualizacao_dados.py
├── ht_salaraio.png
├── ht_distribuicao_salarial.png
└── multiplos_graficos.png
</code></pre>

![Image](https://github.com/user-attachments/assets/80292494-3553-473a-bba2-0e01ce4f35ae)
![Image](https://github.com/user-attachments/assets/5e96e15d-bb81-48f8-8bac-c0085afe4557))
![Image](https://github.com/user-attachments/assets/2a7b490e-6b7b-4a02-bcb1-8dee8ad512d6)

<pre><code>📂 matplotlib
├── uso_matplotlib.py
├── div_escolaridade.png
├── div_escolaridade_2.png
├── div_escolaridade_pizza.png
└── dp_idade_salario.png
</code></pre>

![Escolaridade 1](matplotlib/div_escolaridade.png)
![Escolaridade 2](matplotlib/div_escolaridade_2.png)
![Pizza Escolaridade](matplotlib/div_escolaridade_pizza.png)
![Dispersão Idade x Salário](matplotlib/dp_idade_salario.png)

<pre><code>📂 seaborn
├── uso_seaborn.py
├── disper_idade_salario.png
├── densi_salario.png
├── pairplot.png
├── regre_salario_idade.png
└── countplot.png
</code></pre>

![Dispersão Seaborn](seaborn/disper_idade_salario.png)
![Densidade Salarial](seaborn/densi_salario.png)
![Pairplot](seaborn/pairplot.png)
![Regressão](seaborn/regre_salario_idade.png)
![Countplot](seaborn/countplot.png)

<pre><code>📂 exemplos
├── exemplos_graficos.py
├── hotmap.png
├── countplot.png
└── countplot_legenda.png
</code></pre>

![Heatmap](exemplos/hotmap.png)
![Countplot Exemplo](exemplos/countplot.png)
![Countplot com Legenda](exemplos/countplot_legenda.png)

---

## 🛠️ Bibliotecas Utilizadas

- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

---

## 🚀 Como Executar

1. Clone o repositório
2. Instale as dependências:
3. pip install pandas
4. pip install matplotlib
5. pip install seaborn
