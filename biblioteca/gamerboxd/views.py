from gamerboxd.models import Review, Jogo
from .forms import ReviewForm, JogoForm
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required
def reviewListView(request):
    reviews = Review.objects.filter(
        usuario=request.user).select_related("id_jogo")

    context = {
        "usuario": request.user,
        "reviews": reviews,
    }
    return render(request, "gamerboxd/review_list.html", context)


@login_required
def reviewCreateView(request):
    jogo_id = request.GET.get("jogo")
    initial_data = {}
    if jogo_id:
        initial_data["jogo"] = jogo_id

    if request.method == "POST":
        form = ReviewForm(request.POST, usuario=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.usuario = request.user
            review.save()
            return redirect("review-list")
    else:
        form = ReviewForm(usuario=request.user, initial=initial_data)

    return render(request, "gamerboxd/review_form.html", {
        "form": form,
        "usuario": request.user,
        "edicao": False
    })


@login_required
def reviewEditView(request, id_jogo):
    review = get_object_or_404(Review, usuario=request.user, id_jogo=id_jogo)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review, usuario=request.user)
        if form.is_valid():
            form.save()
            return redirect("review-list")
    else:
        form = ReviewForm(instance=review, usuario=request.user)

    return render(request, "gamerboxd/review_form.html", {
        "form": form,
        "usuario": request.user,
        "edicao": True
    })


@login_required
def reviewDeleteView(request, id_jogo):
    review = get_object_or_404(Review, usuario=request.user, id_jogo=id_jogo)

    if request.method == "POST":
        review.delete()
        return redirect("review-list")

    return render(request, "gamerboxd/review_confirm_delete.html", {
        "review": review,
        "usuario": request.user
    })


def jogoListView(request):
    jogos = Jogo.objects.all()
    context = {
        "jogos": jogos,
    }

    return render(request, "gamerboxd/game_list.html", context)


@login_required
def jogoCreateView(request):
    if request.method == "POST":
        form = JogoForm(request.POST)

        if form.is_valid():
            jogo = form.save(commit=False)
            jogo.save()
            return redirect("jogo-list")
    else:
        form = JogoForm()

    return render(request, "gamerboxd/game_form.html", {"form": form})


@login_required
def redirectToUserReviews(request):
    id_usuario = request.user.id
    return redirect("review-list", id_usuario=id_usuario)


def jogoPageView(request, id_jogo):
    jogo = get_object_or_404(Jogo, id=id_jogo)
    reviews = Review.objects.filter(id_jogo=jogo).select_related("usuario")

    if request.user.is_authenticated:
        user_review = reviews.filter(usuario=request.user).first()

    return render(request, "gamerboxd/jogo_page.html", {
        "jogo": jogo,
        "reviews": reviews,
        "user_review": user_review
    })
