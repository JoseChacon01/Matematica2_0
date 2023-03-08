from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser #Padrão
# class Categoria(models.Model):
#      nome = models.CharField('Nome', max_length=100) #Professor, pesquisador, aluno e administrador
    
    #  def __str__(self):
    #    return self.nome 

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=200)
    idade = models.IntegerField('Idade')
    cpf = models.CharField('CPF', max_length=11, unique=True, primary_key=True) #unique não permite que tenha 2 cadastros com o memso dado, nesse caso, o CPF.
    # categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    USERNAME_FIELD = 'cpf' 

    # class Meta:  
    #     permissions = [
    #         ("Administrador", "Utilização das funções gerais do sistema")
    #     ]

class Acervo_Documentos(models.Model):
    data_acervos_docs = models.DateTimeField('Data_Acervo_Docs')
    autor = models.CharField('Autor', max_length=200)
    titulo = models.CharField('Titulo', max_length=200)
    documento = models.BinaryField(blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
  

class Telefone_Usu (models.Model):
    telefone = models.CharField('Telefone', max_length=20)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Endereco_Usu (models.Model):
    endereco = models.CharField('Endereco', max_length=200)
    numero = models.IntegerField('Numero')
    cep = models.IntegerField('CEP')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Pais_Usu (models.Model):
    nome_pais = models.CharField('Pais', max_length=100)  


class Estado_Usu (models.Model):
    nome_estado = models.CharField('Estado', max_length=100)
    pais = models.ForeignKey(Pais_Usu, on_delete=models.PROTECT)


class Cidade_Usu (models.Model):
    nome_cidade = models.CharField('Cidade', max_length=100)
    estado = models.ForeignKey(Estado_Usu, on_delete=models.PROTECT)


class Bairro_Usu (models.Model):
    nome_bairro = models.CharField('Bairro', max_length=100)
    cidade = models.ForeignKey(Cidade_Usu, on_delete=models.PROTECT)
 




class Dados_Cadastro_PENF (models.Model):
    categoria_cadastro = models.CharField('Categoria_Cadastro', max_length=50)
    data_cadastro = models.DateTimeField('Data_Cadastro') 
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.CharField('Descricao', max_length=600)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Noticias (models.Model):
    imagem_noticia = models.ImageField('Imagem_Noticia')
    cadastro = models.ForeignKey(Dados_Cadastro_PENF, on_delete=models.PROTECT)


class Eventos (models.Model):
    imagem_noticia = models.ImageField('Imagem_Noticia')
    cadastro = models.ForeignKey(Dados_Cadastro_PENF, on_delete=models.PROTECT)


class Pesquisador (models.Model):
    curriculo = models.BinaryField(blank=True)  

class Projetos (models.Model): 
    data_cadastro = models.DateTimeField('Data_Cadastro')  
    proj_para_publicacao = models.BinaryField(blank=True)   
    cadastro = models.ForeignKey(Dados_Cadastro_PENF, on_delete=models.PROTECT) 
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.PROTECT) 

    