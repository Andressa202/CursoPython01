import pandas as pd

#criando um dataframe com pandas
data = {
    "Nome": ["Caio", "Andressa", "Emily", "Davi", "Jesreel", "Eloara", "Alice"],
    "Idade": [15, 20, 25, 30, 35, 40, 45],
    "Salario": [1000, 2000, 3000, 4000, 5000, 6000, 7000]
    }
df = pd.DataFrame(data)

#Exibir o dataframe
print("DataFrame criado: ")
print(df)

#Selecionar uma coluna especifica
print("\nMostra a Coluna nome")
print(df["Nome"])

#filtra linhas 
print("\nPessoas com idade maior que 30")
print(df[df["Idade"] > 30])

#adicionar uma nova coluna 
df["Imposto"] = df["Salario"] * 0.1
print("\nDataframe agora com a coluna imposto")
print(df)

#Media dos salarios 
media_salario = df["Salario"].mean()
print("\nMédia de salario")
print(media_salario)

#Media do Imposto 
media_imposto = df["Imposto"].mean()
print("\nMedia do imposto")
print(media_imposto)

#Salvando o dataframe em arquivo csv
df.to_csv("salarios.csv", index=False)

#carregar arquivo externo de dados
df_externo = pd.read_csv("salarios.csv")
print(df_externo)

