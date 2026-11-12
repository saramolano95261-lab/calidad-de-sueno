import pandas as pd

ruta = "https://raw.githubusercontent.com/saramolano95261-lab/calidad-de-sueno/cabd169ed6091815e87b10198c01828f45aef157/Sleep_health_and_lifestyle_dataset.csv"
df = pd.read_csv(ruta)

print("="*50)
print(df.head())
print("="*50)

print("="*50)
print(df.info())
print("="*50)

print("="*50)
print(df.describe())
print("="*50)

print("="*50)
print(df.columns)
print("="*50)

print("="*50)
print(df.isnull().sum())
print("="*50)

print("="*50)
print(df.shape)
print("="*50)

print("="*50)
print(df["Occupation"])
print("="*50)

print("="*50)
print(df[["Occupation","Age"]])
print("="*50)

print("="*50)
print(df[df["Occupation"] == "Engineer"])
print("="*50)