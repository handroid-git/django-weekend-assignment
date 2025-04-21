from django.shortcuts import render
from .models import Quote
import random

# Create your views here.
def homepage(request):
    quotes = list(Quote.objects.all())
    spotlight_quote = random.choice(quotes) if quotes else None
    return render(request, 'quote/home.html', {'quotes': quotes, 'spotlight': spotlight_quote})