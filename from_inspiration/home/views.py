from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView

from home.froms import CommentForm
from home.models import Card, Category


# Create your views here.
class ProductsList(ListView):
    model = Card
    template_name = 'home/list_of_pictures.html'
    context_object_name = 'cards'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()  # Получаем изначальный QuerySet всех карточек

        category_slug = self.request.GET.get('category')  # Получаем выбранную категорию из параметра запроса

        if category_slug:  # Если указана категория, фильтруем карточки по ней
            queryset = queryset.filter(category__slug=category_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Получаем все категории
        context['selected_category'] = self.request.GET.get('category')  # Получаем выбранную категорию из GET-параметра
        return context


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
