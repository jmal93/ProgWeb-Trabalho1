from django.test import TestCase
from gamerboxd.models import Jogo, Usuario, Review, User
from gamerboxd.forms import ReviewForm


class ReviewFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(
            username='user1',
            password='password123'
        )
        cls.usuario1 = Usuario.objects.create(
            user=cls.user1,
            nome='joao',
            email='joao@email.com'
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
        form = ReviewForm(data=data, initial={'id_usuario': self.usuario1})

        self.assertTrue(form.is_valid())

    def test_review_erro_review_duplicado(self):
        Review.objects.create(
            id_jogo=self.jogo1,
            id_usuario=self.usuario1,
            nota=7,
            descricao='bom'
        )
        data = {
            "id_jogo": self.jogo1.id,
            "nota": 7,
            "descricao": "bom"
        }
        form = ReviewForm(data=data, initial={'id_usuario': self.usuario1})
        self.assertFalse(form.is_valid())
        self.assertIn(
            "Esse usuário já fez uma review para esse jogo.",
            form.errors["__all__"]
        )
