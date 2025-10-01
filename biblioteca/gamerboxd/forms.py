from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["id_jogo", "nota", "descricao"]

    def clean(self):
        cleaned_data = super().clean()
        usuario = self.initial.get("id_usuario")
        jogo = cleaned_data.get("id_jogo")

        if not self.instance.pk:
            if Review.objects.filter(id_usuario=usuario, id_jogo=jogo).exists():
                raise forms.ValidationError("Esse usuário já fez uma review para esse jogo.")

        return cleaned_data