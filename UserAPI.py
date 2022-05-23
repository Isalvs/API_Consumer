# An user api with some kind of cli 

from time import sleep
import requests
from requests import Session

import User
import json
import os


def listAllUsers():
    request = requests.get(base_url )
    users = json.loads(request.content)
    for user in users:
        print(user)
    sleep(2)
    print('=-=' * 25)
    # print(users[0])


def showUserById(id: str) -> Session:
    request = requests.get(base_url + f'?id={id}')
    user = json.loads(request.content)
    return user


def createUser(user: object) -> object:
    requests.post(base_url, data=json.dumps(user.__dict__))
    return requests.session()


def editUserData(id, user):
    requests.put(base_url + f'?id={id}', data=json.dumps(user.__dict__))


def deleteUser(id: str) -> str:
    requests.delete(base_url + f'?id={id}')
    return requests


base_url = 'http://localhost:3002/api/users'

if __name__ == '__main__':
    print('Vamos consumir uma API')
    os.system('pause')
    while True:

        print('''
O que você deseja fazer?
        
[ 1 ] - Listar usuários
[ 2 ] - Cadastrar usuário
[ 3 ] - Editar dados de usuário 
[ 4 ] - Mostrar dados de usuário específico
[ 5 ] - Deletar usuário
[ 6 ] - Sair do programa''')

        ans = str(input('Insira um número -> '))

        if ans.isnumeric():
            if int(ans) == 1:
                print('Listar todos os usuários: ')
                listAllUsers()

            elif int(ans) == 2:

                print('Cadastrar Usuário')
                name = str(input('Informe o nome do usuário: ')).strip()
                passwd = str(input('Informe a senha: ')).strip()
                confPasswd = str(input('Confirme a senha: ')).strip()
                if passwd == confPasswd:
                    createUser(User.User(name, confPasswd))

                listAllUsers()

                sleep(3)

            elif int(ans) == 3:
                print('\b')
                print('Editar Usuário')
                print('''Qual Dado gostaria de editar?
[ 1 ] - Nome
[ 2 ] - senha
[ 3 ] - Ambos
[ 4 ] - Sair
                ''')
                resp = int(input('-> '))

                if resp == 1:
                    name = str(input('Nome: ')).strip()
                    editUserData('6bPQlC0McsmPjKRQ', User.User(name, '1234'))
                elif resp == 2:
                    passwd = str(input('Senha: ')).strip()
                    editUserData('6bPQlC0McsmPjKRQ', User.User('Ismael', passwd))

                elif resp == 3:
                    name = str(input('Name: ')).strip()
                    passwd = str(input('Senha: ')).strip()
                    editUserData('6bPQlC0McsmPjKRQ', User.User(name, passwd))

                elif resp == 4:
                    pass

                listAllUsers()
                sleep(3)

            elif int(ans) == 4:
                print('Usuário específico')
                showUserById('6bPQlC0McsmPjKRQ')

            elif int(ans) == 5:
                print('Deletar Usuário')
                deleteUser('6bPQlC0McsmPjKRQ')
                sleep(2)
                listAllUsers()

            elif int(ans) == 6:
                print('Saindo do programa')
                sleep(2)
                break

            else:
                print('Opção Inválida')

        else:
            print('Não é um número')

    print('Tchau Brigado!!!')
