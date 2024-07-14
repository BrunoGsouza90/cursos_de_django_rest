'''
    Importação da biblioteca Django Ninja.
'''
from ninja import Router

'''
    Importação dos parâmetros estabelecidos no esquema "UserSchema".
'''
from .schemas import UserSchema

'''
    Importação da tabela do Banco de Dados "User".
'''
from .models import User

'''
    Importação da biblioteca Django que vai fazer a criptografia
        das senhas dos clientes ao enviar os dados para o Django.
'''
from django.contrib.auth.hashers import make_password

'''
    Importação da biblioteca de validações do Django, dando enfâse
        aos erros de validação, para chamarmos em casos de erro
        as importações falhas de usuários com uma mensagem mais
        amigável.
'''
from django.core.exceptions import ValidationError

'''
    Criação da variável "users_router" que está recebendo a instância Router
        que seria o nosso "Controlador de Tráfego" em meios as nossas rotas.
'''
users_router = Router()

'''
    Criação de uma função que será responsável por receber as requisições
        do usuário e retornar uma resposta. 
    Está função estará decorada com a rota "users_router" que será um metódo 
        POST onde o usuário estará enviando informações. Está rota passará um
        STATUS em forma de dicionário com uma resposta 200, que indicará que 
        tudo ocorreu corretamente.
    Caso os dados informados pelo cliente sejam inválidos a rota passará um
        STATUS HTTP em forma dicionário com uma resposta 400, que indicará
        que o usuário informou dados inválidos.
    Caso de qualquer outro tipo de erro daremos o STATUS HTTP de resposta
        em formato de dicionário 500 que indicará um erro no lado do 
        servidor.
'''
@users_router.post('', response={200: dict, 400: dict, 500: dict})
#   É necessário na nossa API trabalharmos sempre com esquemas,
#       que seria basicamente um padrão de dados que iremos receber
#       na nossa requisição, então utilizaremos uma variável que
#       irá receber todos esses dados.
#   Essa variável será impletamentada apartir dos esquemas que já
#       vem implementados nas configurações do Django Ninja.
#   Para realizarmos essa operação criaremos no nosso APP um novo
#       arquivo chamado de "schemas".
def create_user(request, user:UserSchema):
    
    '''
        Criação de um print para verificarmos o que está acontecendo
            com os dados após o envio como resposta ao cliente.
    '''
    print(user.dict())









    '''
        Podemos criar dessa maneira dados no nosso usuário
            de maneira específica. 
    '''
    # Obs.: Comentamos pois essa não será a maneira como vamos
    #           trabalhar, pois queremos importar todos os dados.
    #           e existe a maneira abaixo que é mais fácil.
    #user = User(

    '''
        Criação de um usuário apartir dos dados enviados pelo
            cliente.
    '''
        #first_name = user.first_name
        #cpf = user.cpf
    #)










    '''
        Porem podemos utilizar está maneira, onde todos os dados
            são jogados em um dicionário e descompactados esses
            dados com **.
    '''
    user = User(**user.dict())

    '''
        Criação de um print para a verificação da criptografia de
            senha administrada pelo Django Framework para o nosso
            usuário.
        Ao verificar o terminal após o envio do cadastro pelo
            cliente REST verificamos a senha criptografada.
    '''
    print(make_password(user.password))

    '''
        Atribuição da senha criptografada no Banco de Dados.
    '''
    user.password = make_password(user.password)

    '''
        Criação de um try execept do python para uma mensagem
            mais amigável ao usuário após os erros de validação.
        Aqui fazemos a tentiva de validação.
    '''
    try:
            
        #   Chamada de todas as validações do nosso "validators.py"
        #       para a tabela "User".
        
        user.full_clean()
    
        #   Caso as validações deem errado. Caíremos nesse termo de
        #       excessão.

    except ValidationError as e:
        
        #   Criação de um print para o teste da mensagem de erro
        #       no nosso próprio terminal.
        print(e.message_dict)

        #   Retornando um STATUS HTTP 400 informando um erro do
        #3      usuário.
        return 400, {'errors': e.message_dict}
    
        #   Caso de outro tipo de erro que não seja de validação, iremos
        #   retornar a resposta de STATUS HTTP 500 que indica ao cliente
        #   um erro no lado do servidor.
    except Exception as e:

        return 500, {'errors': 'Erro interno do servidor, contrate um adm'}

    '''
        E por fim salvamos.
    '''
    user.save()

    '''
        Resposta de retorno para o cliente REST de uma maneira mais
            amigável.
    '''
    return {'ok': 'ok'}

#   Após todas as configurações, ao fazermos um post nesse modelo:
'''
{
  "username": "caio",
  "firts_name": "Caio",
  "last_name": "Sampaio",
  "email": "caio@email.com",
  "password": "1234",
  "cpf": "111"
}
'''
#   Iremos perceber que recebemos um STATUS de resposta HTTP 200,
#       indicando que deu tudo certo no nosso Cliente REST.
#   E no nosso terminal recebemos algo assim...
'''
   {'username': 'caio', 'first_name': None, 'last_name': 'Sampaio', 
   'cpf': '111', 'email': 'caio@email.com', 'password': '1234'} 
'''
#   Indicando que os dados foram enviados no padrão que 
#       precisavamos. Assim os dados a mais que são enviados por
#       acaso são desconsiderados e trazendo uma resposta de erro
#       400 ao cliente, indicando que ele enviou mais ou menos dados
#       que o especificado.