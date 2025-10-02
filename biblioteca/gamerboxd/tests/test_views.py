from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from gamerboxd.models import Jogo, Usuario, Review


class ViewsTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'biblioteca/homePage.html')


class RegistroViewTests(TestCase):
    def test_registro_get(self):
        response = self.client.get(reverse('sec-registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registro.html')

    def test_registro_post_valido(self):
        data = {
            'username': 'teste',
            'password1': 'SenhaForte123',
            'password2': 'SenhaForte123',
        }
        response = self.client.post(reverse('sec-registro'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home-page'))
        self.assertTrue(User.objects.filter(username='teste').exists())


class LoginViewTests(TestCase):
    def test_profile_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


class ProfileViewTests(TestCase):
    def test_profile_get(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')


class ReviewViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.user1 = User.objects.create_user(
            username='user1',
            password='password123'
        )
        cls.user2 = User.objects.create_user(
            username='user2',
            password='password123'
        )
        cls.superuser = User.objects.create_superuser(
            username='admin',
            password='password123'
        )

        cls.usuario1 = Usuario.objects.create(
            user=cls.user1,
            nome='joao',
            email='joao@email.com'
        )
        cls.usuario2 = Usuario.objects.create(
            user=cls.user2,
            nome='maria',
            email='maria@email.com'
        )

    def setUp(self):
        self.jogo1 = Jogo.objects.create(
            nome="Super Mario Odyssey",
            desenvolvedora="Nintendo",
            dtLanc="2013-09-07",
            genero="Plataforma"
        )
        self.jogo2 = Jogo.objects.create(
            nome="Mortal Kombat",
            desenvolvedora="Warner Bros",
            dtLanc="2023-02-14",
            genero="Luta"
        )

        self.review1 = Review.objects.create(
            id_usuario=self.usuario1,
            id_jogo=self.jogo1,
            nota=10,
            descricao="bom"
        )
        self.review2 = Review.objects.create(
            id_usuario=self.usuario2,
            id_jogo=self.jogo2,
            nota=0,
            descricao="ruim"
        )

    def test_usuario_acessa_proprias_reviews(self):
        self.client.login(username="user1", password="password123")
        response = self.client.get(
            reverse('review-list', kwargs={"id_usuario": self.usuario1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "bom")

    def test_usuario_nao_acessa_review_de_outro_usuario(self):
        self.client.login(username="user1", password="password123")
        response = self.client.get(
            reverse('review-list', kwargs={"id_usuario": self.usuario2.id}))
        self.assertEqual(response.status_code, 403)

    def test_superusuario_acessa_review_de_outro_usuario(self):
        self.client.login(username="admin", password="password123")
        response = self.client.get(
            reverse('review-list', kwargs={"id_usuario": self.usuario2.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ruim")
