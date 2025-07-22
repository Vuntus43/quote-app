from django.db import models
from django.core.exceptions import ValidationError

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    weight = models.PositiveIntegerField(default=1)
    views = models.PositiveIntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
        constraints =[
            models.UniqueConstraint(fields=['text', 'source'],
                                    name = 'unique_quote_per_source')
        ]


    def __str__(self):
        return f'{self.text[:100]}...({self.source})'

    def clean(self):
        if Quote.objects.filter(source = self.source).exclude(pk = self.pk).count() >=3:
            raise ValidationError(f'Нельзя добавить больше 3 цитат для источника "{self.source}"')