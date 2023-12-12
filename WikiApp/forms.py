from .models import Page,WikiDataModel
#import forms
from django import forms


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'the_title',
        ]

from markdownx.fields import MarkdownxFormField
class CustomWikiDataForm(forms.ModelForm):
    class Meta:
        model = WikiDataModel
        fields = '__all__'
        widgets = {
            'last_modified': forms.TextInput(attrs={'readonly': True}),
        }
        content = MarkdownxFormField()

