from django.urls import path
from .views import quote_list, quote_create, top_quotes, vote_quote

urlpatterns = [
    path('', quote_list, name='home'),
    path('add/', quote_create , name='quote_create'),
    path('top/', top_quotes, name='top_quotes'),
    path('vote/<int:pk>/', vote_quote, name='vote_quote'),

]