from django.shortcuts import render
from gamerboxd.models import Review

from .models import Usuario, Review
from .forms import ReviewForm

from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def reviewListView(request, id_usuario):
    usuario = get_object_or_404(Usuario, id=id_usuario)

    if not request.user.is_superuser and request.user.id != usuario.id:
        return HttpResponseForbidden("Você não tem permissão para ver as reviews de outro usuário.")

    reviews = Review.objects.filter(id_usuario=usuario).select_related("id_jogo")
    
    context = {
        "usuario": usuario,
        "reviews": reviews,
    }
    return render(request, "gamerboxd/review_list.html", context)

def reviewCreateView(request, id_usuario):
    usuario = get_object_or_404(Usuario, id=id_usuario)

    if request.method == "POST":
        form = ReviewForm(request.POST, initial={"id_usuario": usuario})
        if form.is_valid():
            review = form.save(commit=False)
            review.id_usuario = usuario
            review.save()
            return redirect("review-list", id_usuario=id_usuario)
    else:
        form = ReviewForm(initial={"id_usuario": usuario})

    return render(request, "gamerboxd/review_form.html", {
        "form": form,
        "usuario": usuario
    })

@login_required
def redirectToUserReviews(request):
    id_usuario = request.user.id
    return redirect("review-list", id_usuario=id_usuario)