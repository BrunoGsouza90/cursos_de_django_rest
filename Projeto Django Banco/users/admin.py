'''
    Aqui faremos todos os nossos registros do Banco de Dados
        para serem monitorados pelo Django Admin na rota "admin/"
'''
from django.contrib import admin

'''
    Importação da tabela "User" do Banco de Dados.
'''
from users.models import User


'''
    Registro da tabela "User" do Banco de Dados no modelo Admin.
'''
admin.site.register(User)