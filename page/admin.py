from django.contrib import admin
from .models import User,Article

class userAdmin(admin.ModelAdmin):
    list_display= ('nom','email')

admin.site.register(User, userAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom','description','image','auteur')

admin.site.register(Article, ArticleAdmin)

