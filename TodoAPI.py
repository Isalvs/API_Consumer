#Todo API to be consumed

import os
import requests
import User
import json


def listar_dados():
    request = requests.get(base_url)
    todos = json.loads(request.content)
    print(todos)
    print(todos[0]['titulo'])
    print(todos[0]['descricao'])


def buscar_dados_id(id):
    request = requests.get(base_url + f'?id={id}')
    todo = json.loads(request.content)
    print(todo)
    print(todo['titulo'])
    print(todo['descricao'])


def cadastrar_dados(tarefa):
    requests.post(base_url, data=json.dumps(tarefa.__dict__))


def editar_dados(id, tarefa):
    requests.put(base_url + f'?id={id}', data=json.dumps(tarefa.__dict__))


def remover_dado(id):
    requests.delete(base_url + f'?id={id}')


base_url = 'http://localhost:3002/api/todo'


if __name__ == '__main__':

    listar_dados()
