import requests

# Fazendo a solicitação HTTP para a API
URL = "https://randomuser.me/api/?results=500"
response = requests.get(URL)
data = response.json()

data_types = data['results']

data_list = []

for user in data_types:
    user_info = {
        "Nome": user['name']['first'] + " " + user['name']['last'],
        "Gênero": user['gender'],
        "Email": user['email'],
        "Usuário": user['login']['username'],
        "Senha": user['login']['password'],
        "Telefone": user['phone'],
        "Celular": user['cell'],
        "Data de Nascimento": user['dob']['date'],
        "Idade": user['dob']['age'],
        "Endereço": {
            "Rua": user['location']['street']['name'],
            "Número": user['location']['street']['number'],
            "Cidade": user['location']['city'],
            "Estado": user['location']['state'],
            "País": user['location']['country'],
            "Código Postal": user['location']['postcode']
        },
        "Nacionalidade": user['nat'],
        "Identidade": {
            "Número": user['id']['value'],
            "Tipo": user['id']['name']
        },
        "Foto": user['picture']['large']
    }
    data_list.append(user_info)

print(data_list[0])