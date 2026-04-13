import pandas as pd
from faker import Faker
import random

fake = Faker("pt_BR")

dados = []

doencas = ["Gripe", "Covid-19", "Pneumonia", "Fratura", "Hipertensão"]
sexos = ["M", "F"]
status_lista = ["Internado", "Alta"]
convenios = ["SUS", "Unimed", "Bradesco Saúde", "Amil", "SulAmérica"]
tipos_atendimento = ["Emergência", "Consulta", "Internação"]


def gerar_dados_fisicos(idade):
    if idade <= 2:
        peso = round(random.uniform(5, 12), 1)
        altura = round(random.uniform(0.7, 0.9), 2)

    elif idade <= 5:
        peso = round(random.uniform(10, 20), 1)
        altura = round(random.uniform(0.85, 1.1), 2)

    elif idade <= 12:
        peso = round(random.uniform(20, 50), 1)
        altura = round(random.uniform(1.1, 1.5), 2)

    elif idade <= 18:
        peso = round(random.uniform(45, 80), 1)
        altura = round(random.uniform(1.5, 1.9), 2)

    elif idade <= 60:
        peso = round(random.uniform(50, 120), 1)
        altura = round(random.uniform(1.5, 2.0), 2)

    else:
        peso = round(random.uniform(45, 100), 1)
        altura = round(random.uniform(1.4, 1.9), 2)

    return peso, altura


for i in range(100):
    data_entrada = fake.date_between(start_date="-2y", end_date="today")
    data_alta = fake.date_between(start_date=data_entrada, end_date="today")

    idade = random.randint(0, 100)
    peso, altura = gerar_dados_fisicos(idade)

    doenca = random.choice(doencas)


    if doenca == "Fratura":
        custo = round(random.uniform(1000, 100000), 2)
    elif doenca in ["Gripe", "Hipertensão"]:
        custo = round(random.uniform(100, 1000), 2)
    else:
        custo = round(random.uniform(500, 5000), 2)

    linha = {
        "ID_Paciente": i + 1,
        "Nome": fake.name(),
        "Idade": idade,
        "Sexo": random.choice(sexos),
        "Doenca": doenca,
        "Medico_Responsavel": fake.name(),
        "Tempo_Internacao": random.randint(0, 30),
        "Peso": peso,
        "Altura": altura,
        "Tipo_Atendimento": random.choice(tipos_atendimento),
        "Convenio": random.choice(convenios),
        "Data_Entrada": data_entrada,
        "Data_Alta": data_alta,
        "Status": random.choice(status_lista),
        "Numero_Exames": random.randint(0, 20),
        "Custo_Tratamento": custo
    }

    dados.append(linha)

df = pd.DataFrame(dados)

df = df[df["Idade"] >= 0]
df = df[df["Peso"] > 0]
df = df[df["Altura"] > 0]
df = df[df["Data_Alta"] >= df["Data_Entrada"]]

df.reset_index(drop=True, inplace=True)
df.to_excel("base_dados_hospital.xlsx", index=False)


