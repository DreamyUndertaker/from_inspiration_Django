from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView

from home.forms import CommentForm
from home.models import Card, Category


# Create your views here.
class ProductListView(ListView):
    template_name = 'home/list_of_pictures.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = self.category
        return context

    def get_queryset(self):
        self.category = None
        self.categories = Category.objects.all()
        self.products = Card.objects.all()  # Используем все объекты Card

        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            self.products = self.products.filter(category=self.category)
        return self.products


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
