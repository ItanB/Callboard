from django import forms
from django.core.exceptions import ValidationError

from .models import Ad, Reply


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'categories',
            'description',
            'price',
            'file',
            'created_at',
        ]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = [
            'author',
            'post',
            'reply_text'
        ]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("reply_text")

        if content is None:
            raise ValidationError(
                "Описание не должно быть пустым."
            )

        return cleaned_data
