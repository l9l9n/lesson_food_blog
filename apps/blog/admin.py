from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Food, Comment, Category, Post


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Food)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'food_name',
        'photo',
        'description',
        'category',

    ]


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'food',
        'text',
        'created',
        'updated',

    ]


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'slug',
        'icon',
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    text = forms.CharField(widget=CKEditorWidget())
    list_display = [
        'id',
        'author',
        'title',
        'short_text',
        # 'text',
        'created',
        'updated',
        # 'photo',
        'get_html_photo',
        'is_draft',
        'category',
    ]

    form = PostAdminForm
    
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
