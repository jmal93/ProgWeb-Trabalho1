from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ViewsTests(TestCase):
    def test_home_sec(self):
        response = self.client.get(reverse('sec-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/homeSec.html')


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
        self.assertRedirects(response, reverse('sec-home'))
        self.assertTrue(User.objects.filter(username='teste').exists())
