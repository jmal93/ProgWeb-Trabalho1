from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text="Insira o nome")
    email = models.EmailField(max_length=254, help_text="Insira o email")

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text="Insira o nome do jogo")
    genero = models.EmailField(max_length=254, help_text="Insira o genero do jogo")
    desenvolvedora = models.EmailField(max_length=254, help_text="Insira a desenvolvedora do jogo")
    dtNasc = models.DateField(
        help_text='Data de lancamento no formato DD/MM/AAAA',
        verbose_name='Data de lancamento')


    def __str__(self):
        return self.nome
    

class Review(models.Model):
    id_jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.IntegerField(help_text="Insira a nota")
    descricao = models.CharField(max_length=256, help_text="Insira a descricao")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_jogo', 'id_usuario'], name='unique_jogo_usuario_combination'
            )
        ]

    def __str__(self):
        return (self.id_jogo, self.id_usuario)