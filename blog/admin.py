from django.contrib import admin
from .models import UserProfile, Category, Article


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'avatar', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'content']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
