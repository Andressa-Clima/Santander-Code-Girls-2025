import json
from faker import Faker
import random

fake = Faker('pt_BR')

notas = []
for i in range(5):
    notas.append({
        "id": f"NF-{i+1:03}",
        "cliente": fake.name(),
        "valor": round(random.uniform(100, 5000), 2),
        "data_emissao": fake.date_this_year().isoformat()
    })

with open("../data/notas_fiscais_2025.json", "w", encoding="utf-8") as f:
    json.dump(notas, f, indent=4, ensure_ascii=False)

print("Arquivo notas_fiscais_2025.json gerado com sucesso!")
