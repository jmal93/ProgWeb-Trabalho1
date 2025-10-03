from django.urls import path
from gamerboxd.views import (
    reviewListView,
    reviewCreateView,
    reviewEditView,
    reviewDeleteView,
    jogoListView,
    jogoCreateView,
    jogoPageView
)

urlpatterns = [
    path("reviews/", reviewListView, name="review-list"),
    path("reviews/new/", reviewCreateView, name="review-create"),
    path("reviews/<int:id_jogo>/edit/", reviewEditView, name="review-edit"),
    path("reviews/<int:id_jogo>/delete/", reviewDeleteView, name="review-delete"),
    path("jogos/", jogoListView, name="jogo-list"),
    path("jogos/new", jogoCreateView, name="jogo-create"),
    path("jogos/<int:id_jogo>/", jogoPageView, name="jogo-page"),
]
