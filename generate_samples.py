# Python script to generate sample data, it simulates the data of N users

import random
import json

course_names = [
    "Python para iniciantes",
    "Introdução à ciência de dados",
    "Banco de dados",
    "Java avançado",
    "Web development",
    "Design gráfico",
    "Machine Learning",
    "Análise de dados com R",
    "Estatística básica",
    "Front-end development",
    "Back-end development",
    "Deep Learning",
    "Big Data",
    "Inteligência Artificial",
    "Data Science com Python",
    "Banco de dados NoSQL",
    "Desenvolvimento mobile",
    "Segurança da informação",
    "Cloud computing",
    "UX/UI Design",
]

cities = [
    "São Paulo", 
    "Rio de Janeiro", 
    "Belo Horizonte", 
    "Porto Alegre"
]

def generate_random_users(num_users, min_courses_per_user, max_courses_per_user) -> list[dict]:
    users = []
    for i in range(num_users):
        print(f"Criando usuário {i+1}/{num_users}", end="\r")
        num_courses_per_user = random.randint(min_courses_per_user, max_courses_per_user)
        user = {
            "nome": f"Usuário {i}",
            "idade": random.randint(18, 65),
            "cidade": random.choice(cities),
            "cursos": [
                {
                    "nome": random.choice(course_names),
                    "avaliacao": round(random.uniform(1, 5), 1)
                }
                for j in range(num_courses_per_user)
            ]
        }
        users.append(user)
    print("Usuários criados com sucesso")
    return users

num_additional_users = 100000

min_courses_per_user = 3
max_courses_per_user = 10
additional_users = generate_random_users(num_additional_users, min_courses_per_user, max_courses_per_user)


print("Salvando arquivo json...")
with open("sample_data.json","w") as file:
    json.dump(additional_users, file)