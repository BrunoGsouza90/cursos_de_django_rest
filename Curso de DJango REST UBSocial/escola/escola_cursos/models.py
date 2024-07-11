from django.db import models

class Base(models.Model):
    ''' Neste exemplo a data atual será salva apenas uma única vez. '''
    criacao = models.DateField(auto_now_add=True)
    ''' Neste exemplo a data atual será renovada toda vez que o sistema
        atualizar. '''
    atualizacao = models.DateField(auto_now=True)
    ''' Se nenhum valor for mencionado ele receberá True automaticamente. '''
    ativo = models.BooleanField(default=True)

    class Meta:
        ''' O modelo abstract na "class Meta" determina que o Django não
                crie uma tabela para esse models; e este models poderá
                ser utilizado e mencionado livremente em outras tabelas
                ou models.'''
        abstract = True


''' Criação de uma class recebendo a herença da "class Base" que é uma class
        com modelos abstratos. '''
class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        ''' Determina que o nome da tabela seja apresentada na página admin
                no singular como 'Curso' . '''
        verbose_name = 'Curso'
        ''' Determina que o nome da tabela seja apresentada na página admin
                no plural como 'Cursos' . '''  
        verbose_name_plural = 'Cursos'
    ''' Determinando qual a descrição será dada para cada dado apresentado
            na tabela na página admin. '''   
    def __str__(self):
        return f'{self.titulo}'


class Avaliacao(Base):
    ''' "related_name" - Permiti que na tabela "Curso" seja usada os atributos
            da tabela "Avaliacao" mencionando "avaliacoes" .'''
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ''' Ao fazer uma avaliação será possível fazer apenas um cadastro
                para cada email e curso específico. '''
        unique_together = ['email', 'curso']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'