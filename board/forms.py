from django import forms
from board.models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'description',
            'price',
            # 'categories',
            'created_at',
        ]


class NewAd(forms.ModelForm):
    pass
