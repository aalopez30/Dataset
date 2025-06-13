import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL RAW desde GitHub
url = "https://github.com/aalopez30/Dataset/blob/a7a3a07658564cbfc0672d0b838a0618a9e00420/procesos_activos.csv?raw=true"

# Leer CSV
df = pd.read_csv(url)
df = df.dropna()
df = df.drop_duplicates()

# Estadísticas básicas
print("Media:\n", df.mean(numeric_only=True))
print("\nMediana:\n", df.median(numeric_only=True))
print("\nModa:\n", df.mode(numeric_only=True).iloc[0])
print("\nDesviación estándar:\n", df.std(numeric_only=True))

# Correlación
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación entre Variables")
plt.tight_layout()
plt.show()
