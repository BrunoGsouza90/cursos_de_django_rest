'''
    Importação da biblioteca do Banco de Dados Django Framework.
'''
from django.db import models

'''
    Importação da biblioteca padrão de autentificação do Django
        Framework.
'''
from django.contrib.auth. models import AbstractUser

'''
    Importação da biblioteca que será responsável por manter todos
        os valores monetários em formato decimal.
'''
from decimal import Decimal

'''
    Importação da biblioteca de validações, dando enfâse a nossa
        função "validate_cpf" que fará a validação do CPF do usuário.
'''
from .validators import validade_cpf

'''
    Criação de uma Classe que está herdando da Classe "AbstractUser"
     do Django Framework.
    Está tabela estará acrescentando colunas a tabela já existente
        "AbstractUser".
'''
class User(AbstractUser):

    '''
        Aqui fazemos mensão  ao validators = []...
        Será onde faremos a verificação de validação do nosso CPF.
    '''
    cpf = models.CharField(max_length=14, unique=True, validators=[validade_cpf])
    email = models.EmailField(unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))

    '''
        Para não salvarmos no Banco de Dados o CPF com pontos e
            traços, iremos descrever essa coluna, salvando os
            dados sem pontos e traços.
    '''
    def save(self, *args, **kwargs):
        '''
            Realizando a exclusão dos pontos e traços da coluna
                CPF.
        '''
        self.cpf = self.cpf.replace('.','').replace('-','')
        '''
            Salvando o contéudo no Banco de Dados.
        '''
        super(User, self).save(*args, **kwargs)

    '''
        Criação do método pagar, que será onde o dinheiro será
            diminuído na conta do usuário.
    '''
    def pay(self, value: Decimal):

        '''
            Garantindo que o método passado é uma instância de
                valores decimais.
        '''
        if not isinstance(value, Decimal):
            '''
                Mensagem de erro caso o valor não seja uma instãncia
                    de valores decimais.
            '''
            raise TypeError('Value deve ser um Decimal')
        
        '''
            Se a instância for verdadeira substrairemos o valor
                descrito para a conta do usuário.
        '''
        self.amount -= value

        # Obs.: Não iremos salvar os dados diretamente no Banco de
        #           de Dados, para fazermos um método mais seguro
        #           de atomacidade.


    '''
        Criação do método receber, que será onde o dinheiro será
            aumentado na conta do usuário.
    '''
    def pay(self, value: Decimal):

        '''
            Garantindo que o método passado é uma instância de
                valores decimais.
        '''
        if not isinstance(value, Decimal):
            '''
                Mensagem de erro caso o valor não seja uma instãncia
                    de valores decimais.
            '''
            raise TypeError('Value deve ser um Decimal')
        
        '''
            Se a instância for verdadeira acrecentaremos o valor
                descrito para a conta do usuário.
        '''
        self.amount += value

        # Obs.: Não iremos salvar os dados diretamente no Banco de
        #           de Dados, para fazermos um método mais seguro
        #           de atomacidade.


# Obs.: Caso executarmos o makemigrations nesse momento dará um
#           erro de autentificação pois não informamos ao Django
#           que queremos utilizar a nossa própria classe de "Users".
#       Para mais informações confira a linha 32 do "settings.py".