# Neste arquivo gerenciaremos as rotas do Django Ninja.

'''
    Importação da biblioteca do Django Ninja API.
'''
from ninja import NinjaAPI

'''
    Criação da instância do Django Ninja que será onde adicionaremos uma
        rota.
'''
api = NinjaAPI()

'''
    Criação da rota "users/" que será redirecionada para a rota 
        "users_router".
'''
api.add_router('users/', users_router)