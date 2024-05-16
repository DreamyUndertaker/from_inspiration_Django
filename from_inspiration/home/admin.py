from django.contrib import admin

from home.models import Card, Comment, Category, UserProfile


# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Card, CardAdmin)

admin.site.register(Comment)

admin.site.register(UserProfile)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
