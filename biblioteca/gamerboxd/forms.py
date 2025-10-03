from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["id_jogo", "nota", "descricao"]

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        usuario = self.usuario
        jogo = cleaned_data.get("id_jogo")

        if not self.instance.pk and usuario and jogo:
            if Review.objects.filter(usuario=usuario, id_jogo=jogo).exists():
                raise forms.ValidationError("Esse usuário já fez uma review para esse jogo.")

        return cleaned_data