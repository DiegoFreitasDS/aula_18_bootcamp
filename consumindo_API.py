import requests
import json

from pydantic import BaseModel

# Contrato de dados | Schema de dados ! View da API
class RandonSchema(BaseModel):
    nome: str
    genero: str
    email: str
    dt_nasc: str
    # rua: str
    # numero: str
    # cidade: str
    # estado: str
    # país: str
    # cep: int

    class Config:
        from_attributes = True

def pegar_info(id: int) -> RandonSchema:
    
    # Fazendo a solicitação HTTP para a API
    URL = (f"https://randomuser.me/api/?results={id}")
    response = requests.get(URL)
    data = response.json()

    # data_types = data['results']

    data_list = []

    for user in data["results"]:
        data_list.append((user['name']['first'] + " " + user['name']['last']))  # Nome
        data_list.append(user['gender'])  # Gênero
        data_list.append(user['email'])  # Email
        data_list.append(user['dob']['date'])  # Data de Nascimento
        data_list.append(user['location']['street']['name'])  # Rua
        # data_list.append(user['location']['street']['number'])  # Número
        # data_list.append(user['location']['city'])  # Cidade
        # data_list.append(user['location']['state'])  # Estado
        # data_list.append(user['location']['country'])  # País
        # data_list.append(user['location']['postcode'])  # Código Postal
        types = ', '.join(str(v) for v in data_list)
        return RandonSchema(type=types, 
                            nome=user['name']['first'] + " " + user['name']['last'],
                            genero=user['gender'],
                            email=user['email'],
                            dt_nasc=user['dob']['date'], 
                            # rua=data['location']['street']['name'],
                            # #numero=data['location']['street']['number'],
                            # cidade=data['location']['city'],
                            # estado=data['location']['state'],
                            # país=data['location']['country'],
                            # cep=data['location']['postcode'],
                            input_type=dict)
                            

if __name__ == "__main__":
    print(pegar_info(100))
    # print(pegar_info(50))
    # print(pegar_info(15))