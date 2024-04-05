# aula_18_bootcamp


**.append()** aceita apenas *um argumento*, que é o item a ser adicionado à lista. **Se você deseja adicionar vários itens ao mesmo tempo**, você precisa *passá-los como um único argumento*, como uma lista ou uma tupla.

````

for users in data_types:
    user_info = {
        "Nome:": users['name']['first'] + " " + users['name']['last'],
        "Gênero:": users['gender']
    }
    data_list.append(user_info)

````