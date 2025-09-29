from django.urls import path
from .views import reviewListView, reviewCreateView, redirectToUserReviews

urlpatterns = [
    path("reviews/<int:id_usuario>/", reviewListView, name="review-list"),
    path("reviews/<int:id_usuario>/new/", reviewCreateView, name="review-create"),
    path("reviews/", redirectToUserReviews, name="user-reviews"),
]
