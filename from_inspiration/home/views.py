from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView

from .forms import CommentForm, UserUpdateForm, ProfileUpdateForm
from .models import Card, Category


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


class UserProfileDetailView(DetailView):
    template_name = 'home/user_detail.html'
    context_object_name = 'user'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['user_cards'] = Card.objects.filter(author=user)
        context['all_categories'] = Category.objects.all()
        return context


class UserSettingsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'home/settings.html'
    context_object_name = 'user'
    form_class = ProfileUpdateForm
    model = User

    def get_success_url(self):
        return reverse_lazy('user-settings', kwargs={'pk': self.get_object().id})

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context
