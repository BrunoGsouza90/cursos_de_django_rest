'''
    Criaremos nesse arquivo nossos esquemas do Django Ninja.
'''

'''
    Importação das bibliotecas:
    ModelSchema = Aqui utilizamos alguma tabela do Banco de Dados
        pra gerar os esquemas.
    Schema = Aqui definimos do 0 quais dados receberemos na 
        requisição.
'''
from ninja import ModelSchema, Schema

'''
    Importação da tabela do Banco de Dados "User".
'''
from .models import User

'''
    Criação de uma classe que estará herdando os dados da tabela
        User padrão do Django.
'''
class UserSchema(ModelSchema):

    '''
        Aqui defineremos as configurações adicionais da tabela User.
    '''
    class Meta:
        '''
            Específicação de qual tabela do Banco de Dados estamos
                trabalhando.
        '''
        # Obs.: Os nossas tabelas da tabela "User" estão
        #           especificadas na tabela padrão do Django "User"; 
        # e no nosso models.py adicionamos colunas a essa tabela.
        model = User
    
        '''
            Definição de quais colunas queremos receber da tabela
                "User".
        '''
        fields = [
            'username',
            'first_name',
            'last_name',
            'cpf',
            'email',
            'password',
        ]