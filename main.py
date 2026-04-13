import pandas as pd
from faker import Faker
import random

fake = Faker("pt_BR")

dados = []

doencas = ["Gripe", "Covid-19", "Pneumonia", "Fratura", "Diabetes", "Hipertensão"]
sexos = ["M", "F"]
status_lista = ["Internado", "Alta"]
convenios = ["SUS", "Unimed", "Bradesco Saúde", "Amil", "Particular"]
tipos_atendimento = ["Emergência", "Consulta", "Internação"]

for i in range(100):
    data_entrada = fake.date_between(start_date="-2y", end_date="today")
    data_alta = fake.date_between(start_date=data_entrada, end_date="today")

    linha = {
        "ID_Paciente": i + 1,
        "Nome": fake.name(),
        "Idade": random.randint(0, 100),
        "Sexo": random.choice(sexos),
        "Doenca": random.choice(doencas),
        "Medico_Responsavel": fake.name(),
        "Tempo_Internacao": random.randint(0, 30),
        "Peso": round(random.uniform(3, 120), 1),
        "Altura": round(random.uniform(0.5, 2.0), 2),
        "Tipo_Atendimento": random.choice(tipos_atendimento),
        "Convenio": random.choice(convenios),
        "Data_Entrada": data_entrada,
        "Data_Alta": data_alta,
        "Status": random.choice(status_lista),
        "Numero_Exames": random.randint(0, 20),
        "Custo_Tratamento": round(random.uniform(100, 20000), 2)
    }

    dados.append(linha)

df = pd.DataFrame(dados)
df = df[df["Idade"] >= 0]
df = df[df["Peso"] > 0]
df = df[df["Altura"] > 0]
df = df[df["Data_Alta"] >= df["Data_Entrada"]]

df.reset_index(drop=True, inplace=True)
df.to_excel("base_dados_hospital.xlsx", index=False)

