# Neste arquivo gerenciaremos as rotas do Django Ninja.

'''
    Importação da biblioteca do Django Ninja API.
'''
from ninja import NinjaAPI

'''
    Dentro do app "users" teremos um arquivo chamado "api" e dentro desse
        arquivo teremos uma chamada para a rota "users_router".
'''
from users.api import users_router

'''
    Criação da instância do Django Ninja que será onde adicionaremos uma
        rota.
'''
api = NinjaAPI()

'''
    Criação da rota "users/" que será redirecionada para a rota 
        "users_router". Está variável será criada no app "users".
'''
api.add_router('users/', users_router)