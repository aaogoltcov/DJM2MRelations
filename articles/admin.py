from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, FieldScope, ArticleField


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_article = False
        is_main_bool_count = int()
        for form in self.forms:
            try:
                if str(form.cleaned_data['is_main_bool']) == 'True':
                    is_main_bool_count += 1
                else:
                    pass
                if form.cleaned_data['id']:
                    is_article = True
                else:
                    pass
            except KeyError:
                pass
        if is_main_bool_count == 1:
            pass
        elif is_main_bool_count > 1 and is_article == True:
            raise ValidationError('Параметр Основной должен быть заполнен не более одного раза')
        elif is_article == True:
            raise ValidationError('Параметр Основной не заполнен')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = ArticleField
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(FieldScope)
class FieldScopeAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
