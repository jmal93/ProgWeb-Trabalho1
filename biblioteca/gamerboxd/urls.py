from django.urls import path
from .views import *

urlpatterns = [
    path("reviews/<int:id_usuario>/", reviewListView, name="review-list"),
    path("reviews/<int:id_usuario>/new/", reviewCreateView, name="review-create"),
    path("reviews/", redirectToUserReviews, name="user-reviews"),
    path("reviews/<int:id_usuario>/<int:id_jogo>/edit/", reviewEditView, name="review-edit"),
    path("reviews/<int:id_usuario>/<int:id_jogo>/delete/", reviewDeleteView, name="review-delete"),
]
