from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text_preview', 'author', 'source',
                    'weight', 'views', 'likes', 'dislikes', 'created_at')
    search_fields = ('text', 'source')
    list_filter = ('created_at',)

    def text_preview(self, obj):
        return obj.text[:50] + '...'
    text_preview.short_description = 'Цитата'