import random
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Quote
from .forms import QuoteForm


def quote_list(request):
    quotes = Quote.objects.all()
    if not quotes:
        return render(request, 'quotes/quote_list.html', {'quote': None})

    selected_quote = random.choices(
        quotes,
        weights=[q.weight for q in quotes],
        k=1
    )[0]

    selected_quote.views += 1
    selected_quote.save(update_fields=["views"])

    return render(request, 'quotes/quote_list.html', {'quote': selected_quote})


@require_POST
def vote_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    action = request.POST.get('action')

    if action == 'like':
        quote.likes += 1
    elif action == 'dislike':
        quote.dislikes += 1

    quote.save()
    return redirect('home')


def top_quotes(request):
    quotes = Quote.objects.order_by('-likes')[:10]
    return render(request, 'quotes/top_quotes.html', {'quotes': quotes})

def quote_create(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm()

    return render(request, 'quotes/quote_form.html', {'form': form})