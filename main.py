import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")

filtro_coluna = dados["Team/NOC"]
print(filtro_coluna)

filtro_ouro = dados[dados["Gold Medal"] > 10]
print(filtro_ouro)

filtro_continente = dados[dados["Continent"] == "Europe"]
print(filtro_continente)

media_por_equipe = dados.groupby("Team/NOC")["Gold Medal"].mean()
print(media_por_equipe)

contagem_por_continente = dados.groupby("Continent").size()
print(contagem_por_continente)

contagem_por_continente.to_csv("novosdados.csv", index=False)

plt.figure(figsize=(10, 6))
filtro_coluna.value_counts().plot(kind='bar')
plt.xlabel('Continente')
plt.ylabel('Contagem')
plt.title('Contagem de Equipes por Continente')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 8))
filtro_continente.groupby('Continent')['Gold Medal'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição das Medalhas de Ouro por Continente')
plt.ylabel('')
plt.show()

plt.figure(figsize=(10, 6))
df_media_por_equipe = pd.DataFrame({'Team/NOC': media_por_equipe.index, 'Gold Medal': media_por_equipe.values})
plt.scatter(df_media_por_equipe['Team/NOC'], df_media_por_equipe['Gold Medal'])
plt.xlabel('Equipe')
plt.ylabel('Média de Medalhas de Ouro')
plt.title('Média de Medalhas de Ouro por Equipe')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()