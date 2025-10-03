from django.test import TestCase
from gamerboxd.models import Jogo, Review, User
from gamerboxd.forms import ReviewForm, JogoForm


class ReviewFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(
            username='user1',
            password='password123'
        )
        cls.jogo1 = Jogo.objects.create(
            nome="Super Mario Odyssey",
            desenvolvedora="Nintendo",
            dtLanc="2013-09-07",
            genero="Plataforma"
        )

    def test_review_form_valido(self):
        data = {
            "id_jogo": self.jogo1.id,
            "nota": 8,
            "descricao": "bom"
        }
        form = ReviewForm(data=data, usuario=self.user1)

        self.assertTrue(form.is_valid())

    def test_review_erro_review_duplicado(self):
        Review.objects.create(
            id_jogo=self.jogo1,
            usuario=self.user1,
            nota=7,
            descricao='bom'
        )
        data = {
            "id_jogo": self.jogo1.id,
            "nota": 7,
            "descricao": "bom"
        }
        form = ReviewForm(data=data, usuario=self.user1)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "Esse usuário já fez uma review para esse jogo.",
            form.errors["__all__"]
        )


class JogoFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "nome": "Celeste",
            "genero": "Plataforma",
            "desenvolvedora": "Maddy Makes Games",
            "dtLanc": "2018-01-25"
        }

    def test_jogo_form_valido(self):
        form = JogoForm(data=self.data)

        self.assertTrue(form.is_valid())

    def test_erro_jogo_duplicado(self):
        Jogo.objects.create(
            nome="Celeste",
            genero="Plataforma",
            desenvolvedora="Maddy Makes Games",
            dtLanc="2018-01-25"
        )
        form = JogoForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "Esse jogo já existe",
            form.errors["__all__"]
        )
