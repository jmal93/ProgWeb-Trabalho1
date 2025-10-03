from django.contrib import admin

# Register your models here.

from gamerboxd.models import Jogo, Review

admin.site.register(Jogo)
admin.site.register(Review)