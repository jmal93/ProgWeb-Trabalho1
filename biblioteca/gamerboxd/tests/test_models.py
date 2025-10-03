from django.test import TestCase
from django.contrib.auth.models import User
from gamerboxd.models import Jogo, Review


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
        cls.user = User.objects.create(
            username="joao_user", password="password123")
        cls.jogo = Jogo.objects.create(nome='GTA', genero="Acao",
                                       desenvolvedora="Rockstar", dtLanc="2013-09-07")

        Review.objects.create(id_jogo=cls.jogo, usuario=cls.user,
                              nota=10, descricao="teste")

    def test_retorna_nome(self):
        review = Review.objects.get(id=1)
        nome_esperado = f'Review de {review.usuario} para {review.id_jogo}'
        self.assertEqual(nome_esperado, str(review))
