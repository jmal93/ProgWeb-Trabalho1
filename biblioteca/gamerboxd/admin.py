from django.contrib import admin

# Register your models here.

from gamerboxd.models import Usuario, Jogo, Review

admin.site.register(Usuario)
admin.site.register(Jogo)
admin.site.register(Review)