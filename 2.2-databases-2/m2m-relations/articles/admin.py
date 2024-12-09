from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1
                    if count > 1:
                        raise ValidationError('Основной тэг может быть только один.')
            if count == 0:
                raise ValidationError('Основной тег не назначен.')
            else:
                pass
        return super().clean()

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = (ScopeInlineFormset)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    

