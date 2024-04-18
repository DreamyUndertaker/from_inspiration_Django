from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView

from home.froms import CommentForm
from home.models import Card


# Create your views here.
class ProductsList(ListView):
    model = Card
    template_name = 'home/list_of_pictures.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Перенаправление на страницу входа, если пользователь не аутентифицирован
        return super().dispatch(request, *args, **kwargs)


class CardDetailView(View):
    template_name = 'home/card_detail.html'

    def get(self, request, slug):
        card = Card.objects.get(slug=slug)
        comments = card.comments.all()
        form = CommentForm()
        return render(request, self.template_name, {'card': card, 'comments': comments, 'form': form})

    def post(self, request, slug):
        card = Card.objects.get(slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.card = card
            comment.author = request.user
            comment.save()
            return redirect('card_detail', slug=slug)

        comments = card.comments.all()
        return render(request, self.template_name, {'card': card, 'comments': comments, 'form': form})
