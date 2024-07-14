'''
    Nesse arquivo implantaremos nossas funções de validação.
'''

'''
    Importação da biblioteca de validações do Django Framework.
'''
from django.core.exceptions import ValidationError

'''
    Criação da função que receberá o valor do CPF que será salvo
        no Banco de Dados. Caso ele receba um erro dará um erro
        de validação.
'''
def validade_cpf(value):
    '''
        Criação de uma variável todos os digitos da variável CPF.
    '''
    cpf = ''.join([char for char in value if char.isdigit()])

    '''
        Verificação se o número de CPF tem 11 dígitos.
    '''
    if len(cpf) != 11:
        print('Aqui 3')
        raise ValidationError('CPF inválido')
    
    '''
        Verificação se todos os dígitos do CPF são iguais.
    '''
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido')
    
    '''
        Criação de uma função que fará o calculo dos dígitos de
            verificação.
        Função básica para validação de CPF em python.
    '''
    def calcular_digito(cpf, multiplicadores):
        soma = sum(
            int(cpf[i]) * multiplicadores[i]
            for i in range(len(multiplicadores))
        )
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    '''
        Multiplicadores para o primeiro digito de verificação.
    '''
    multiplicadores_primeiro = list(range(10, 1, -1))
    primeiro_digito = calcular_digito(cpf, multiplicadores_primeiro)

    '''
        Multiplicador para o segundo dígito de verificação.
    '''
    multiplicadores_segundo = list(range(11, 1, -1))
    segundo_digito = calcular_digito(cpf, multiplicadores_segundo)

    '''
        Verificando se os dígitos calculados são iguais aos informados.
    '''
    if not (cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito)):
        raise ValidationError('CPF inválido')