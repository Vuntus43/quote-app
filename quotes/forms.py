from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'source', 'weight']
        labels = {
            'text': 'Текст цитаты',
            'author': 'Автор',
            'source': 'Источник',
            'weight': 'Вес',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
            'weight': forms.NumberInput(attrs={'min': 1}),
        }

    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if Quote.objects.filter(text__iexact=text).exists():
            raise forms.ValidationError("Такая цитата уже существует.")
        return text

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get('source')
        if source:
            existing_count = Quote.objects.filter(source__iexact=source).count()
            if existing_count >= 3:
                raise forms.ValidationError("У этого источника уже есть 3 цитаты. Больше добавить нельзя.")
        return cleaned_data
