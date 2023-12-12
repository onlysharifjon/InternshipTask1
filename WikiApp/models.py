from django.db import models

# Create your models here.

class Page(models.Model):
    the_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.the_title}"

from markdownx.models import MarkdownxField
class WikiDataModel(models.Model):
    theme = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="theme")
    title = models.CharField(max_length=255)
    content = MarkdownxField()
    last_modified = models.DateTimeField(auto_now=True,editable=True)

    def __str__(self):
        return f"{self.title}"
