from django.test import TestCase
from django.contrib.auth.models import User
from gamerboxd.models import Jogo, Usuario, Review


class UsuarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="joao", password="senha@123")
        Usuario.objects.create(nome="Joao", email="teste@teste.com", user=user)

    def test_retorna_nome(self):
        usuario = Usuario.objects.get(id=1)
        nome_esperado = f'{usuario.nome}'
        self.assertEqual(nome_esperado, str(usuario))


class JogoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Jogo.objects.create(nome='GTA', genero="Acao",
                            desenvolvedora="Rockstar", dtLanc="2013-09-07")

    def test_retorna_nome(self):
        jogo = Jogo.objects.get(id=1)
        nome_esperado = f'{jogo.nome}'
        self.assertEqual(nome_esperado, str(jogo))


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            username="joao_user", password="password123")
        cls.usuario = Usuario.objects.create(
            user=user, nome="Joao", email="teste@teste.com")
        cls.jogo = Jogo.objects.create(nome='GTA', genero="Acao",
                                       desenvolvedora="Rockstar", dtLanc="2013-09-07")

        Review.objects.create(id_jogo=cls.jogo, id_usuario=cls.usuario,
                              nota=10, descricao="teste")

    def test_retorna_nome(self):
        review = Review.objects.get(id=1)
        nome_esperado = f'Review de {review.id_usuario} para {review.id_jogo}'
        self.assertEqual(nome_esperado, str(review))
